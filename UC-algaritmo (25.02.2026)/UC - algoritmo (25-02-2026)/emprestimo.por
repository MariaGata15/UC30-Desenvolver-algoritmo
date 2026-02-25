programa {
    funcao inicio() {
        escreva("Qual o valor da casa: ")
        leia(ValorCasa)

        escreva("Qual o seu salário? ")
        leia(salario)

        escreva("Em quantos anos voc~e deseja pagar?")
        leia(anos)

        meses = anos * 12
        prestacao = valorCasa / meses

        se(prestacao <= salario * 0.30) {
            escreva("Empréstimo aprovado \n")
        } senao {
            escreva("Empréstimo negado \n")        }
    }
}