package com.main;

import com.data.Suplier;
import com.data.UID;
import com.entity.Player;
import com.object.SuperObject;
import com.tile.TileManager;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JPanel;

public class GamePanel extends  JPanel implements Runnable{
    // SCREEN SETTINGS
    final int originalTileSize = 16;// 16 x 16 tiles
    final int scale = 4                      ; // AUMENTAR O TAMANHO DOS PIXEIS

    public final int tileSize = originalTileSize * scale;
    public final int maxScreenCol = 16;
    public final int maxScreenRow = 12;
    // <---16--->
    // / \
    //  |
    //  12
    //  |
    // \ /
    public final int screenWidth = maxScreenCol*tileSize; // 768 pixeis
    public final int screenHeight = maxScreenRow*tileSize; // 576 pixeis
    //768x576

    //WORLD SETTINGS
    public final int maxWorldCol = 50;
    public final int maxWorldRow = 50;

    //fps
    public final int FPS = 60;

    UID[] typeUID = UID.values();
    public Suplier UIDSuplier = new Suplier();

    KeyHandler keyH = new KeyHandler();
    Sound sound = new Sound();
    TileManager tileManager = new TileManager(this);
    public CollisionChecker cChecker = new CollisionChecker(this);
    public AssetSetter aSetter = new AssetSetter(this);
    Thread gameThread;

    //Entity and Object
    public Player player = new Player(this,keyH);
    public SuperObject obj[] = new SuperObject[10];
    
    
    
    


    public GamePanel() {
        // setar o tamanho da tela
        this.setPreferredSize(new Dimension(screenWidth,screenHeight));
        this.setBackground(Color.black);
        
        // para melhora performance
        this.setDoubleBuffered(true);
       
       
       //colocar o KeyHandler como o listener das keys
        this.addKeyListener(keyH);
        // game panel pode receber key input
        this.setFocusable(true);
    }

    public void setupGame(){
        aSetter.setObject();
        playMusic(0);
    }


    public void startGameThread(){
        gameThread = new Thread(this);
        gameThread.start();
    
    }

    @Override
    public void run(){
        
        double drawInterval = 1000000000/FPS;
        //0.01666 second
        double delta = 0;
        long lastTime = System.nanoTime();
        long currentTime;

        long timer = 0;
        int drawCount = 0;
        
        while(gameThread != null){
            //1 UPDATE: update information such as character positions
            // 2 DRAW: draw the screen with the updated information
            
            currentTime = System.nanoTime();
            delta += (currentTime-lastTime)/drawInterval;
            timer += (currentTime-lastTime);
            lastTime = currentTime;

            if (delta >=1){
                update();
                repaint();
                delta--;
                drawCount++;
            }

            if ( timer >= 1000000000){
                System.out.println("FPS:"+drawCount);
                timer=0;drawCount=0;
            }

            



        }

    }

    public void update(){
        player.update();



    }

    @Override
    public void paintComponent(Graphics g){
        super.paintComponent(g);
        // são a mesma coisa mas o graphics2D tem alguns funções a mais
        Graphics2D g2 = (Graphics2D)g;
        
        //TILE MAP
        tileManager.draw(g2);

        //OBJECT
        for(int i=0; i<obj.length;i++){
            if(obj[i]!=null){
                obj[i].draw(g2,this);
            }
        }

        //PLAYER
        player.draw(g2);

        
        
        
        //libera recurso que não precisa mais
        g2.dispose();




    }
    

    public void playMusic(int i){
        sound.setFile(i);
        sound.play();
        sound.loop();
    }
    
    public void playSE(int i){
        sound.setFile(i);
        sound.play();

    }

    public void stopMusic(){
        sound.stop();
    }



}
