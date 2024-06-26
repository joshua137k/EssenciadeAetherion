package com.entity;

import com.data.UID;
import com.main.GamePanel;
import com.main.KeyHandler;
import com.object.OBJ_Doorclosed;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Player extends Entity{

    GamePanel gp;
    KeyHandler keyH;

    public final int screenX;
    public final int screenY;
    public int hasKey = 0;

    public Player(GamePanel gp,KeyHandler keyH){
        this.gp=gp;
        this.keyH=keyH;

        screenX = (gp.screenWidth/2) - (gp.tileSize/2);
        screenY = (gp.screenHeight/2)- (gp.tileSize/2);

        solidArea = new Rectangle(18,25,26,28);
        solidAreaDefaultX = solidArea.x;
        solidAreaDefaultY = solidArea.y;
        

        setDefaultValues();
        getPlayerImage();
    }

    public void setDefaultValues(){
        worldX =gp.tileSize* 4;
        worldY =gp.tileSize* 3;
        speed = 4;
        direction = "down";
    }

    public void getPlayerImage(){
        try {
            //WALK UP
            

            up0 = ImageIO.read(new File("res/Player/walk/walkU0.png"));
            up1 = ImageIO.read(new File("res/Player/walk/walkU1.png"));
            up2 = ImageIO.read(new File("res/Player/walk/walkU2.png"));
            up3 = ImageIO.read(new File("res/Player/walk/walkU3.png"));

            //WALK DOWN
            down0 = ImageIO.read(new File("res/Player/walk/walkD0.png"));
            down1 = ImageIO.read(new File("res/Player/walk/walkD1.png"));
            down2 = ImageIO.read(new File("res/Player/walk/walkD2.png"));
            down3 = ImageIO.read(new File("res/Player/walk/walkD3.png"));

            //WALK LEFT
            left0 = ImageIO.read(new File("res/Player/walk/walkA0.png"));
            left1 = ImageIO.read(new File("res/Player/walk/walkA1.png"));
            left2 = ImageIO.read(new File("res/Player/walk/walkA2.png"));
            left3 = ImageIO.read(new File("res/Player/walk/walkA3.png"));

            //WALK RIGHT
            right0 = ImageIO.read(new File("res/Player/walk/walkR0.png"));
            right1 = ImageIO.read(new File("res/Player/walk/walkR1.png"));
            right2 = ImageIO.read(new File("res/Player/walk/walkR2.png"));
            right3 = ImageIO.read(new File("res/Player/walk/walkR3.png"));
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void update(){
        if(keyH.upPressed==true || keyH.downPressed==true || keyH.leftPressed==true || keyH.rightPressed==true){
        
            if(keyH.upPressed==true){
                direction = "up";
            }
            else if(keyH.downPressed==true){
                direction = "down";
                
            }
            else if(keyH.leftPressed==true){
                direction = "left";
                
            }
            else if(keyH.rightPressed==true){
                direction = "right";
                
            }


            
            //Check Tile Collision
            collisionOn=false;
            gp.cChecker.checkTile(this);

            //Check object Collision
            int objIndex = gp.cChecker.checkObject(this,true);
            pickUpObject(objIndex);

            if (!collisionOn){
                switch (direction) {
                    case "up":
                        worldY -= speed;
                        break;
                    case "down":
                        worldY += speed;
                        break;
                    case "left":
                        worldX -= speed;
                        break;
                    case "right":
                        worldX += speed;
                        break;
                }
                
            }
            // if collision is false player can move
            
            spriteCounter++;
            if(spriteCounter > gp.FPS/8){
                spriteNum++;
                if (spriteNum>4){
                    spriteNum=1;
                }
                spriteCounter=0;
            }
        }
    
    }

    public void pickUpObject(int index){
        if (index>=0){
            UID objectName = gp.obj[index].name;
            
            switch (objectName) {
                case UID.Key:
                    hasKey++;
                    gp.playSE(1);
                    gp.obj[index]=null;
                    System.out.println("KEY:"+hasKey);
                    break;
                case UID.Doorclosed:
                    if(hasKey>0){
                        gp.playSE(3);
                        gp.obj[index].collision=false;
                        gp.obj[index].image =((OBJ_Doorclosed)gp.obj[index]).imageOpen;
                        hasKey--;
                        System.out.println("OPEN");
                        System.out.println("KEY:"+hasKey);

                    }
                
                    break;
                case UID.Chestclosed:
                
                    break;
                
                case UID.Boot:
                    speed += 1;
                    gp.playSE(2);
                    gp.obj[index]=null;
                    break;

            }

        }

    }

    public void draw(Graphics2D g2){
        
        BufferedImage image = null;
        switch (direction) {
            case "up":
                if(spriteNum == 1){
                    image = up0;
                }
                else if(spriteNum == 2){
                    image = up1;
                }
                else if(spriteNum == 3){
                    image = up2;
                }
                else if(spriteNum == 4){
                    image = up3;
                }
                break;
            case "down":
                if(spriteNum == 1){
                    image = down0;
                }
                else if(spriteNum == 2){
                    image = down1;
                }
                else if(spriteNum == 3){
                    image = down2;
                }
                else if(spriteNum == 4){
                    image = down3;
                }
                break;
            case "left":
                if(spriteNum == 1){
                    image = left0;
                }
                else if(spriteNum == 2){
                    image = left1;
                }
                else if(spriteNum == 3){
                    image = left2;
                }
                else if(spriteNum == 4){
                    image = left3;
                }
                break;
            case "right":
                if(spriteNum == 1){
                    image = right0;
                }
                else if(spriteNum == 2){
                    image = right1;
                }
                else if(spriteNum == 3){
                    image = right2;
                }
                else if(spriteNum == 4){
                    image = right3;
                }
                break;
        }
        g2.drawImage(image, screenX,screenY, gp.tileSize,gp.tileSize,null);
        //g2.fillRect(solidArea.x+screenX,solidArea.y+screenY,solidArea.width,solidArea.height);

    }
}
