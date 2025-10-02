from tarefa_composta import TarefaComposta
from tarefa_simples import TarefaSimples

def main(): 
    """Cria uma arvore com 12 tarefas e 4 níveis"""
    #nivel 1
    projeto = TarefaComposta("Desenvolvimento de Software")
    #nivel 2
    planejamento = TarefaComposta("Planejamento")
    desenvolvimento = TarefaComposta("Desenvolvimento")
    testes = TarefaComposta("Testes")
    implantacao = TarefaComposta("Implantação")
    #nivel 3
    analise_requisitos = TarefaComposta("Análise de Requisitos")
    design_sistema = TarefaSimples("Design do Sistema")
    #nivel 4
    req_funcionais = TarefaSimples("Requisitos Funcionais")
    req_nao_funcionais = TarefaSimples("Requisitos Não Funcionais")
    #nivel 3
    backend = TarefaComposta("Backend")
    frontend = TarefaSimples("Frontend")
    #nivel 4
    api = TarefaSimples("API")
    banco_dados = TarefaSimples("Banco de Dados")
    #nivel 3
    testes_unitarios = TarefaSimples("Testes Unitários")
    testes_integracao = TarefaSimples("Testes de Integração")
    deploy = TarefaSimples("Deploy")

    #montagem da arvore
    print("\nMontagem da árvore de tarefas:")

    #nivel 4 -> 3
    analise_requisitos.adicionar(req_funcionais)
    analise_requisitos.adicionar(req_nao_funcionais)
    backend.adicionar(api)
    backend.adicionar(banco_dados)
    #nivel 3 -> 2
    planejamento.adicionar(analise_requisitos)
    planejamento.adicionar(design_sistema)
    desenvolvimento.adicionar(backend)
    desenvolvimento.adicionar(frontend)
    testes.adicionar(testes_unitarios)
    testes.adicionar(testes_integracao)
    implantacao.adicionar(deploy)
    #nivel 2 -> 1
    projeto.adicionar(planejamento)
    projeto.adicionar(desenvolvimento)
    projeto.adicionar(testes)
    projeto.adicionar(implantacao)

    print("\nExibição da árvore de tarefas:")
    print("\n" + "=" * 30)
    projeto.exibir()

    print("\n" + "=" * 40)
    print("TESTE 1: Concluindo tarefas do nível mais baixo")
    print("=" * 40 + "\n")

    req_funcionais.concluir()
    req_nao_funcionais.concluir()

    print("\n--- Estrutura atual ---")
    projeto.exibir()

    print("\n" + "=" * 70)
    print("TESTE 2: Concluindo tarefa composta (Requisitos)")
    print("=" * 70 + "\n")
    analise_requisitos.concluir()

    print("\n--- Estrutura atual ---")
    projeto.exibir()

    #tentando concluir planejamento (deve falhar)
    print("\n" + "=" * 70)
    print("TESTE 3: Tentando concluir tarefa composta (Planejamento) com sub-tarefas não concluídas")
    print("=" * 70 + "\n")
    planejamento.concluir()

    # Concluindo a tarefa pendente
    print("\n" + "=" * 70)
    print("TESTE 4: Concluindo tarefa pendente e tentando novamente")
    print("=" * 70 + "\n")
    design_sistema.concluir()
    planejamento.concluir()

    print("\n--- Estrutura atual ---")
    projeto.exibir()

    print("\n" + "=" * 70)
    print("TESTE 5: Desfazendo conclusão de tarefa composta (Planejamento)")
    print("=" * 70 + "\n")
    req_funcionais.desfazer_conclusao()

    print("\n--- Estrutura atual ---")
    projeto.exibir()
    print(f"\nAnalise de Requisitos concluída? {analise_requisitos.esta_concluida()}")

    #concluindo tarefas restantes
    print("\n" + "=" * 70)
    print("TESTE 6: Concluindo todas as tarefas restantes")
    print("=" * 70 + "\n")
    backend.concluir()
    banco_dados.concluir()
    api.concluir()
    frontend.concluir()
    desenvolvimento.concluir()
    testes_unitarios.concluir()
    testes_integracao.concluir()
    testes.concluir()
    deploy.concluir()
    implantacao.concluir()
    projeto.concluir()
    deploy.concluir()

        # Estrutura final
    print("\n" + "=" * 70)
    print("ESTRUTURA FINAL DO PROJETO")
    print("=" * 70)
    projeto.exibir()
        
    print(f"\n✓ Projeto completo? {projeto.esta_concluida()}")
        
        # Testando consulta de estado
    print("\n" + "=" * 70)
    print("TESTE 7: Consultando estado individual de tarefas")
    print("=" * 70 + "\n")
        
    print(f"Backend concluído? {backend.esta_concluida()}")
    print(f"Frontend concluído? {frontend.esta_concluida()}")
    print(f"Projeto concluído? {projeto.esta_concluida()}")

if __name__ == "__main__":
    main()