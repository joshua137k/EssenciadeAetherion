package com.main;

import javax.swing.JFrame;

public class Main {
    public static void main(String[] args) {
        
        
        
        JFrame window = new JFrame();

        //SETAR O BUTÃO DE DESLIGAR
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // não podemos mudar o tamanho
        window.setResizable(false);

        window.setTitle("See Tesouro");

        GamePanel gamePanel = new GamePanel();

        window.add(gamePanel);

        window.pack();

        //sem especificar a localização ela fica no centro
        window.setLocationRelativeTo(null);

        //janela aparecer
        window.setVisible(true);
        gamePanel.setupGame();
        gamePanel.startGameThread();



    }
}
