// Para ler e escrever dados em Java, aqui na DIO padronizamos da seguinte forma:  
// - new Scanner(System.in): cria um leitor de Entradas, com métodos úteis com prefixo "next"; 
// - System.out.println:.imprime um texto de Saída (Output) e pulando uma linha.   

import java.util.Scanner; 
    
public class Multas {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        int velocidade = leitor.nextInt();
        int multas = leitor.nextInt();
        
        if(velocidade<=80){
          System.out.println(multas + " multas. Nao levou pontos na carteira");
        }else{
          if (velocidade>80 && multas<2) {
            multas++;
            System.out.println(multas + " multas. Nao levou pontos na carteira");
          } else {
            multas++;
            System.out.println(multas + " multas. Levou pontos na carteira");
            
          }
        }
        leitor.close();
    }
}