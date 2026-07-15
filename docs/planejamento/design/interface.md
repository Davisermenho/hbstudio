# CRIANDO A INTERFACE

Para resolver isso de forma elegante e sem precisar instalar pacotes pesados além dos que você já possui (`moviepy`, `Pillow`, `numpy`), podemos usar o **Tkinter**, que é a biblioteca nativa de interfaces gráficas do Python.

## SCRIPT DA INTERFACE

Abaixo, desenvolvi um script completo chamado `interface_analise.py`. Ele cria uma janela onde o analista preenche os dados, carrega o frame exato do vídeo para clicar e desenhar as marcações, gera o JSON automaticamente e já dispara a renderização.

### Como implementar:

1. Salve o código abaixo como `interface_analise.py` na mesma pasta onde estão o seu `editar_video.py` e o `config_exemplo.json`.
2. Execute no terminal: `python interface_analise.py`

### O Código: `interface_analise.py`

```python
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
import subprocess
import sys
from PIL import Image, ImageTk
from moviepy.editor import VideoFileClip

class VideoEditorUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerador de Análise Tática")
        self.geometry("1100x700")
        
        # Variáveis de Estado
        self.video_path = ""
        self.frame_image = None
        self.photo_image = None
        self.video_width = 1280
        self.video_height = 720
        self.canvas_width = 640
        self.canvas_height = 360
        self.scale_x = 1.0
        self.scale_y = 1.0
        
        self.grafismos = []
        self.current_tool = None
        self.click_buffer = []

        self.setup_ui()

    def setup_ui(self):
        # Frame da Esquerda (Formulário)
        frm_form = ttk.Frame(self, padding="10")
        frm_form.pack(side=tk.LEFT, fill=tk.Y)

        # 1. Carregar Vídeo
        ttk.Label(frm_form, text="1. Selecione o Vídeo:").grid(row=0, column=0, sticky="w", pady=(0,5))
        self.lbl_video = ttk.Label(frm_form, text="Nenhum vídeo selecionado", foreground="gray")
        self.lbl_video.grid(row=1, column=0, columnspan=2, sticky="w")
        ttk.Button(frm_form, text="Procurar Vídeo...", command=self.load_video).grid(row=0, column=1, sticky="e")

        # 2. Dados do Clipe
        ttk.Label(frm_form, text="2. Configurações do Clipe:").grid(row=2, column=0, sticky="w", pady=(15,5))
        
        ttk.Label(frm_form, text="Nome do Clipe:").grid(row=3, column=0, sticky="w")
        self.ent_nome = ttk.Entry(frm_form)
        self.ent_nome.insert(0, "clipe_01")
        self.ent_nome.grid(row=3, column=1, sticky="ew")

        ttk.Label(frm_form, text="Atleta:").grid(row=4, column=0, sticky="w")
        self.ent_atleta = ttk.Entry(frm_form)
        self.ent_atleta.grid(row=4, column=1, sticky="ew")

        ttk.Label(frm_form, text="Tipo (acerto/ajuste):").grid(row=5, column=0, sticky="w")
        self.cb_tipo = ttk.Combobox(frm_form, values=["acerto", "ajuste"], state="readonly")
        self.cb_tipo.set("ajuste")
        self.cb_tipo.grid(row=5, column=1, sticky="ew")

        ttk.Label(frm_form, text="Legenda de Abertura:").grid(row=6, column=0, sticky="w")
        self.ent_label = ttk.Entry(frm_form)
        self.ent_label.insert(0, "AJUSTE: Fechar linha de passe")
        self.ent_label.grid(row=6, column=1, sticky="ew")

        # 3. Tempos
        ttk.Label(frm_form, text="Início do Clipe (HH:MM:SS):").grid(row=7, column=0, sticky="w")
        self.ent_inicio = ttk.Entry(frm_form)
        self.ent_inicio.insert(0, "00:00:00.000")
        self.ent_inicio.grid(row=7, column=1, sticky="ew")

        ttk.Label(frm_form, text="Fim do Clipe:").grid(row=8, column=0, sticky="w")
        self.ent_fim = ttk.Entry(frm_form)
        self.ent_fim.insert(0, "00:00:10.000")
        self.ent_fim.grid(row=8, column=1, sticky="ew")

        ttk.Label(frm_form, text="Momento da Análise:").grid(row=9, column=0, sticky="w")
        self.ent_momento = ttk.Entry(frm_form)
        self.ent_momento.insert(0, "00:00:05.000")
        self.ent_momento.grid(row=9, column=1, sticky="ew")

        ttk.Button(frm_form, text="Carregar Frame da Análise ->", command=self.load_frame).grid(row=10, column=0, columnspan=2, pady=5, sticky="ew")

        # 4. Configuração da Câmera Lenta
        ttk.Label(frm_form, text="Legenda da Câmera Lenta:").grid(row=11, column=0, sticky="w", pady=(10,0))
        self.ent_legenda = ttk.Entry(frm_form)
        self.ent_legenda.insert(0, "Posicionamento correto")
        self.ent_legenda.grid(row=11, column=1, sticky="ew", pady=(10,0))

        # Ferramentas Gráficas
        ttk.Label(frm_form, text="3. Adicionar Grafismos:").grid(row=12, column=0, sticky="w", pady=(15,5))
        
        frm_tools = ttk.Frame(frm_form)
        frm_tools.grid(row=13, column=0, columnspan=2, sticky="ew")
        
        ttk.Button(frm_tools, text="🟢 Círculo", command=lambda: self.set_tool("circulo")).pack(side=tk.LEFT, padx=2)
        ttk.Button(frm_tools, text="↗️ Seta", command=lambda: self.set_tool("seta")).pack(side=tk.LEFT, padx=2)
        ttk.Button(frm_tools, text="↗️ Seta Tracejada", command=lambda: self.set_tool("seta_tracejada")).pack(side=tk.LEFT, padx=2)
        ttk.Button(frm_tools, text="Limpar", command=self.clear_grafismos).pack(side=tk.RIGHT, padx=2)

        self.lbl_status = ttk.Label(frm_form, text="Selecione uma ferramenta", foreground="blue")
        self.lbl_status.grid(row=14, column=0, columnspan=2, pady=5)

        # 5. Ação Final
        ttk.Button(frm_form, text="Gerar JSON e Renderizar Vídeo", command=self.generate_and_render, style="Accent.TButton").grid(row=15, column=0, columnspan=2, pady=20, sticky="ew")

        # Frame da Direita (Canvas/Preview)
        frm_preview = ttk.Frame(self, padding="10")
        frm_preview.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        ttk.Label(frm_preview, text="Preview do Frame (Clique para adicionar marcações)").pack(anchor="w")
        
        self.canvas = tk.Canvas(frm_preview, width=self.canvas_width, height=self.canvas_height, bg="black", cursor="crosshair")
        self.canvas.pack(fill=tk.BOTH, expand=True, pady=10)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def load_video(self):
        filepath = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mov")])
        if filepath:
            self.video_path = filepath
            self.lbl_video.config(text=os.path.basename(filepath))

    def load_frame(self):
        if not self.video_path:
            messagebox.showerror("Erro", "Selecione o vídeo primeiro!")
            return
        
        try:
            time_str = self.ent_momento.get()
            clip = VideoFileClip(self.video_path)
            self.video_width, self.video_height = clip.size
            
            # Converter HH:MM:SS para segundos
            partes = time_str.split(":")
            segundos = float(partes[0])*3600 + float(partes[1])*60 + float(partes[2])
            
            frame_np = clip.get_frame(segundos)
            clip.close()

            # Converter para imagem do Pillow e redimensionar para o Canvas
            img = Image.fromarray(frame_np)
            
            # Atualizar Canvas mantendo proporção
            canvas_w = self.canvas.winfo_width()
            canvas_h = self.canvas.winfo_height()
            
            # Calcular escala
            ratio = min(canvas_w / self.video_width, canvas_h / self.video_height)
            new_w = int(self.video_width * ratio)
            new_h = int(self.video_height * ratio)
            
            self.scale_x = self.video_width / new_w
            self.scale_y = self.video_height / new_h

            img_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            self.photo_image = ImageTk.PhotoImage(img_resized)
            
            self.canvas.delete("all")
            self.canvas.create_image(canvas_w//2, canvas_h//2, anchor=tk.CENTER, image=self.photo_image)
            self.grafismos = [] # Limpa grafismos anteriores
            self.lbl_status.config(text="Frame carregado. Selecione uma ferramenta.")

        except Exception as e:
            messagebox.showerror("Erro ao ler frame", str(e))

    def set_tool(self, tool_name):
        self.current_tool = tool_name
        self.click_buffer = []
        if tool_name == "circulo":
            self.lbl_status.config(text="CÍRCULO: Clique no centro do jogador.")
        elif tool_name in ["seta", "seta_tracejada"]:
            self.lbl_status.config(text="SETA: Clique no início (origem) da seta.")

    def on_canvas_click(self, event):
        if not self.current_tool or not self.photo_image:
            return

        # Descobre a coordenada real baseada no offset da imagem no canvas
        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()
        img_w = self.photo_image.width()
        img_h = self.photo_image.height()
        
        offset_x = (canvas_w - img_w) // 2
        offset_y = (canvas_h - img_h) // 2
        
        if event.x < offset_x or event.x > offset_x + img_w or event.y < offset_y or event.y > offset_y + img_h:
            return # Clicou fora do frame

        # Converte a coordenada do clique para a resolução original do vídeo
        real_x = int((event.x - offset_x) * self.scale_x)
        real_y = int((event.y - offset_y) * self.scale_y)

        # Lógica de Ferramentas
        if self.current_tool == "circulo":
            self.grafismos.append({"tipo": "circulo", "x": real_x, "y": real_y, "raio": 50})
            self.canvas.create_oval(event.x-20, event.y-20, event.x+20, event.y+20, outline="yellow", width=3)
            self.lbl_status.config(text="Círculo adicionado!")
            self.current_tool = None
            
        elif self.current_tool in ["seta", "seta_tracejada"]:
            self.click_buffer.append((real_x, real_y, event.x, event.y))
            if len(self.click_buffer) == 1:
                self.lbl_status.config(text="SETA: Agora clique no destino (ponta da seta).")
                self.canvas.create_oval(event.x-3, event.y-3, event.x+3, event.y+3, fill="red")
            elif len(self.click_buffer) == 2:
                p1_real, p2_real = self.click_buffer[0][:2], self.click_buffer[1][:2]
                p1_canvas, p2_canvas = self.click_buffer[0][2:], self.click_buffer[1][2:]
                
                self.grafismos.append({
                    "tipo": self.current_tool,
                    "x1": p1_real[0], "y1": p1_real[1],
                    "x2": p2_real[0], "y2": p2_real[1]
                })
                
                dash = (5,5) if self.current_tool == "seta_tracejada" else None
                self.canvas.create_line(p1_canvas[0], p1_canvas[1], p2_canvas[0], p2_canvas[1], fill="yellow", width=3, arrow=tk.LAST, dash=dash)
                self.lbl_status.config(text="Seta adicionada!")
                self.current_tool = None
                self.click_buffer = []

    def clear_grafismos(self):
        self.grafismos = []
        self.current_tool = None
        self.click_buffer = []
        self.load_frame() # Recarrega o frame limpo

    def generate_and_render(self):
        if not self.video_path:
            messagebox.showerror("Atenção", "Nenhum vídeo selecionado.")
            return
            
        json_data = {
            "video_origem": self.video_path,
            "diretorio_saida": "saida",
            "fps_saida": 30,
            "clipes": [
                {
                    "nome": self.ent_nome.get(),
                    "atleta": self.ent_atleta.get(),
                    "tipo": self.cb_tipo.get(),
                    "label_abertura": self.ent_label.get(),
                    "inicio": self.ent_inicio.get(),
                    "fim": self.ent_fim.get(),
                    "momento_analise": self.ent_momento.get(),
                    "tipo_analise": "slow_motion",
                    "velocidade_slow": 0.5,
                    "janela_analise_segundos": 3.0,
                    "duracao_freeze": None,
                    "grafismos": self.grafismos,
                    "legenda_analise": self.ent_legenda.get()
                }
            ]
        }

        # Salvar JSON
        json_path = "config_gerado_app.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)

        # Chamar script de edição
        self.lbl_status.config(text="Renderizando vídeo... Aguarde.")
        self.update()
        
        try:
            # Chama o seu script editar_video.py passando o JSON gerado
            subprocess.run([sys.executable, "editar_video.py", json_path], check=True)
            messagebox.showinfo("Sucesso!", f"Vídeo renderizado na pasta 'saida/'.\nJSON salvo como {json_path}.")
            self.lbl_status.config(text="Renderização concluída!")
        except Exception as e:
            messagebox.showerror("Erro de Renderização", f"Ocorreu um erro ao chamar o editar_video.py:\n{e}")

if __name__ == "__main__":
    app = VideoEditorUI()
    app.mainloop()

```

### O que essa interface faz por você:

1. **Preenchimento Rápido:** Tem campos para digitar todas as informações necessárias exigidas pelo `config_exemplo.json` (Nome, atleta, legendas, inícios e fins).
2. **Player/Extrator Interno:** Quando o analista preenche o "Momento da Análise" e clica em "Carregar Frame", o script usa o `moviepy` em background para puxar aquele frame exato do vídeo e exibi-lo na tela.
3. **Mapeamento Matemático:** A maior mágica está na escala. Como a janela do programa é menor que um vídeo em Full HD, a interface adapta a imagem. Quando você clica na tela pequena, a matemática de `offset` e `scale_x/y` converte o seu clique para o pixel original exato da gravação original.
4. **UX Fluida:** Se você clicar em "Seta", ela orienta a clicar primeiro na origem (onde o jogador está) e depois no destino (para onde ele deveria ir), desenhando uma prévia amarela e temporária na tela para você ver como ficou.
5. **Automação Completa:** Clicando no botão final, ele pega todos os campos, empacota em um JSON válido (`config_gerado_app.json`) e instantaneamente dispara via `subprocess` o seu código principal (`editar_video.py`), entregando o vídeo pronto na pasta final.