# Estado operacional diário

Este arquivo contém pendências e o modelo de atualização diária. Ele deve ser atualizado após cada jogo e não deve reutilizar automaticamente o estado anterior. Consulte também a programação da competição e as políticas para agentes.

## Registro de estado

| Identificador | Conteúdo |
| --- | --- |
| `STA-CUR-001` | Estado operacional atual |
| `STA-PEN-001` | Pendências críticas |
| `STA-UPD-001` | Ordem de atualização |

## STA-CUR-001 — Estado operacional atual

```yaml
estado_operacional:
  atualizado_em: "2026-07-15T00:00:00-03:00"
  data: "2026-07-13"
  fase_competicao: "Fase classificatória — Grupo A"
  ultimo_resultado: "ACISEG 35 x 24 IDEC — derrota do IDEC"
  posicao_atual: "pendente de atualização da classificação oficial do Grupo A"
  proximo_adversario: "FMO/PORTUGUÊS-PE"
  proximo_jogo:
    data: "2026-07-14"
    horario: "15:30"
    aquecimento: "14:30"
    reuniao_pre_jogo: "pendente de definição"
    saida: "pendente de confirmação"
  confirmacoes:
    transporte: pendente
    almoco: pendente
    jantar: pendente
  atletas_indisponiveis_ou_com_restricoes: []
  scout_disponivel: false
  videos_disponiveis:
    - jogo: "ACISEG 35x24 IDEC — 2026-07-13"
      arquivo: "videos/ACISEG_35x24_IDEC_2026-07-13/ACISEG_35x24_IDEC_2026-07-13.mp4"
      config: "config_exemplo.json"
      clipes:
        - nome: lance_01_transicao_bebe
          atleta: "Bebê"
          tipo: acerto
          status: gerado — aguardando validacao visual
          arquivo_saida: "saida/lance_01_transicao_bebe.mp4"
        - nome: lance_02_leitura_goleiro
          atleta: "Clark"
          tipo: ajuste
          status: gerado — aguardando validacao visual
          arquivo_saida: "saida/lance_02_leitura_goleiro.mp4"
        - nome: lance_03_1x1_continuidade
          atleta: "Cirilo"
          tipo: acerto
          status: gerado — aguardando validacao visual
          arquivo_saida: "saida/lance_03_1x1_continuidade.mp4"
        - nome: lance_05_transicao_iago
          atleta: "Iago"
          tipo: acerto
          status: gerado — aguardando validacao visual
          arquivo_saida: "saida/lance_05_transicao_iago.mp4"
      observacao: >
        infiltracao_bebe.mp4 existe em saida/ mas pertence a uma config anterior
        sem registro rastreavel. Nao deve ser usado como referencia da baseline 0.4.0.
  decisoes_pendentes_da_tecnica:
    - "Definir as prioridades técnicas de correção após a derrota para o ACISEG"
    - "Aprovar o plano de jogo contra o FMO/PORTUGUÊS-PE"
  pendencias_operacionais_criticas:
    - "Atualizar a classificação oficial do Grupo A após a rodada de 13 de julho"
    - "Confirmar jantar de 13 de julho às 18:30"
    - "Confirmar transporte para a cerimônia de abertura de 13 de julho às 20:00"
    - "Confirmar almoço de 14 de julho às 11:30"
    - "Confirmar transporte, ponto de encontro e saída para o jogo de 14 de julho"
    - "Definir horário da reunião pré-jogo contra o FMO/PORTUGUÊS-PE"
    - "Localizar ou confirmar vídeo e scout do FMO/PORTUGUÊS-PE"
    - "Registrar atletas indisponíveis ou com restrições, se houver"
    - "Definir recuperação, hidratação e descanso após o primeiro jogo"
   
```

Valores recomendados para confirmações: `pendente`, `confirmado`, `alterado` ou `cancelado`.

## STA-PEN-001 — Pendências críticas

- confirmação completa dos transportes;
- contato do responsável pelo veículo;
- ponto de encontro e horário real de saída;
- divisão dos quartos;
- dados de saúde e emergência;
- números de camisa e posições;
- correção dos contatos com erro no banco de dados;
- alimentação nos dias condicionais;
- transporte da cerimônia de abertura;
- transporte do FIESC ao restaurante após os jogos;
- logística de retorno em 18 de julho;
- conflito entre premiação e voo;
- atualização dos dias 16, 17 e 18 após cada resultado.

Quando uma pendência afetar o próximo evento, ela deve aparecer antes de assuntos
secundários.

## STA-UPD-001 — Ordem de atualização

Depois de cada jogo, atualizar nesta ordem:

1. resultado;
2. classificação;
3. próximo adversário;
4. próximo horário;
5. alimentação;
6. transporte;
7. descanso;
8. scout.