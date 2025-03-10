=# 🤝 Descritivo do Microserviço “Mentorados”

Este **microserviço** faz parte da **Plataforma de Mentoria** desenvolvida na disciplina de 
**Engenharia de Software com Microsserviços** da **Universidade Presbiteriana Mackenzie**. 
O objetivo do *Serviço de Mentorados* é gerenciar as necessidades e dados referentes aos 
usuários que desejam receber mentoria, incluindo:

- Cadastro de perfis de mentorados  
- Busca e sugestão de mentores compatíveis  
- Histórico de sessões e feedbacks recebidos  
- Armazenamento das preferências e expectativas do mentorado  

---
## Backlog e User Storys
![project flowchart](/imgs/userStoryeBacklog.png)


## Kanban
![project flowchart](/imgs/Kanbanmentorados.jpg)

## 🎯 Objetivos Principais

1. **Gerenciar Perfis de Mentorados**  
   Fornecer endpoints para criação, edição e visualização dos dados de cada mentorado.

2. **Facilitar a Busca de Mentores**  
   Integrar com outros microsserviços (Matching, Agenda, etc.) para sugerir e filtrar mentores 
   conforme a necessidade do mentorado.

3. **Armazenar Histórico e Feedbacks**  
   Registrar as sessões concluídas, manter anotações, acompanhar o progresso e permitir 
   avaliação do mentor.

4. **Oferecer Visão do Próximo Passo**  
   Integrar com o serviço de Agenda ou Notificações para que o mentorado saiba das próximas 
   sessões, prazos e lembretes relevantes.

---

## 👥 Público-Alvo

- **Mentorados**: Usuários que buscam orientação e acompanhamento em determinada área 
  (profissional, acadêmica, pessoal etc.).  
- **Gestor**: Pode analisar dados consolidados dos mentorados, cruzar com o sistema de 
  disponibilidade de mentores e tomar decisões sobre duplas de mentoria.

---

## 🏗️ Arquitetura e Integrações

O *microserviço de Mentorados* se comunica com outros serviços da plataforma, como:

- **Serviço de Autenticação**  
  Para validação de credenciais e controle de acesso (mentorados x mentores x gestores).

- **Serviço de Matching**  
  Para sugerir mentores adequados ao perfil de cada mentorado.

- **Serviço de Agenda**  
  Para agendamentos e confirmações de sessões.

- **Serviço de Notificações**  
  Para avisar os mentorados sobre novas sessões, lembretes ou feedbacks.

Cada serviço funciona de forma independente, possibilitando escalabilidade, baixo acoplamento 
e robustez na aplicação.

---

## 🚀 Metodologia de Desenvolvimento

Adotamos **Scrum** para organizar as sprints e entregar funcionalidades incrementais:

- **Sprint Planning**: Definição de backlog e tarefas do microserviço.  
- **Daily Scrums**: Alinhamento do time, identificação de impedimentos.  
- **Sprint Review e Retrospectiva**: Apresentação do que foi desenvolvido, ajustes e melhorias 
  contínuas.

*(Ver Kanban geral do projeto para detalhes de cada tarefa.)*

---

## ⏰ Entregas e Datas Importantes

No contexto do projeto maior (Plataforma de Mentoria), este microserviço segue o cronograma 
estabelecido pela disciplina, com entregas para cada **MVP**, **deploy** e **apresentação final**.

---

## 🛠️ Tecnologias e Ferramentas

 - Pendente
---

## 📦 Como Executar Localmente

1. Deve-se clonar o repositorio
2. Project from verison control
3. cole a URL e execute

**OBS**: Devem ser criadas branch separadas do MAIN