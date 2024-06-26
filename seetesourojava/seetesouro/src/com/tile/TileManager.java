package com.tile;

import com.data.UID;
import com.main.GamePanel;
import java.awt.Graphics2D;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import javax.imageio.ImageIO;


public class TileManager {

    GamePanel gp;
    public Map<Integer, Tile> tile;
    public int mapTileNum[][];

    public TileManager(GamePanel gp) {
        this.gp = gp;
        tile = new HashMap<>();
        


        mapTileNum = new int[gp.maxWorldCol][gp.maxWorldRow];
        loadMap("res/maps/world01/world.txt");

        getTileImage();

    

    }

    public void loadMap(String path){
        try {
            BufferedReader br = new BufferedReader(new FileReader(path));
            String line;

            int row = 0;
            while ((line = br.readLine())!=null){
                String[] l = line.split(" ");

                for (int col=0;col<l.length;col++){
                    if (row<=gp.maxWorldRow){



                        mapTileNum[col][row]=Integer.parseInt(l[col]);
                    }
                }
                
                
                row++;
                
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }


    public void getTileImage(){
        try {
            
                // 0 Grass
                Tile grass = new Tile();
                grass.image = ImageIO.read(new File(UID.Grass.getPath()));
                grass.id = UID.Grass.ordinal();
                tile.put(grass.id, grass);

                // 1 Stone
                Tile stone = new Tile();
                stone.id = UID.Stone.ordinal();
                stone.image = ImageIO.read(new File(UID.Stone.getPath()));
                stone.collision = true;
                tile.put(stone.id, stone);

                // 2 Water
                Tile water = new Tile();
                water.id = UID.Water.ordinal();
                water.image = ImageIO.read(new File(UID.Water.getPath()));
                water.collision = true;
                tile.put(water.id, water);

                // 3 Dirt
                Tile dirt = new Tile();
                dirt.id = UID.Dirt.ordinal();
                dirt.image = ImageIO.read(new File(UID.Dirt.getPath()));
                tile.put(dirt.id, dirt);

                // 4 Tree
                Tile tree = new Tile();
                tree.id = UID.Tree.ordinal();
                tree.image = ImageIO.read(new File(UID.Tree.getPath()));
                tree.collision = true;
                tile.put(tree.id, tree);

                // 5 Sand
                Tile sand = new Tile();
                sand.id = UID.Sand.ordinal();
                sand.image = ImageIO.read(new File(UID.Sand.getPath()));
                tile.put(sand.id, sand);

                // 6 Floor
                Tile floor = new Tile();
                floor.id = UID.Floor.ordinal();
                floor.image = ImageIO.read(new File(UID.Floor.getPath()));
                tile.put(floor.id, floor);

                // 7 Bush
                Tile bush = new Tile();
                bush.id = UID.Bush.ordinal();
                bush.image = ImageIO.read(new File(UID.Bush.getPath()));
                bush.collision = true;
                tile.put(bush.id, bush);

                // 8 Mussstone
                Tile mussstone = new Tile();
                mussstone.id = UID.Mussstone.ordinal();
                mussstone.image = ImageIO.read(new File(UID.Mussstone.getPath()));
                tile.put(mussstone.id, mussstone);

                            
            
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public void draw(Graphics2D g2){
        for ( int x = 0; x<gp.maxWorldCol;x++){
            for ( int y = 0; y<gp.maxWorldRow;y++){

                int worldX = gp.tileSize*x;
                int worldY = gp.tileSize*y;
                int screenX = worldX - gp.player.worldX + gp.player.screenX;
                int screenY = worldY - gp.player.worldY + gp.player.screenY;


                if ( worldX + gp.tileSize > gp.player.worldX - gp.player.screenX &&
                     worldX - gp.tileSize < gp.player.worldX + gp.player.screenX &&
                     worldY + gp.tileSize > gp.player.worldY - gp.player.screenY &&
                     worldY - gp.tileSize < gp.player.worldY + gp.player.screenY){
                        Tile t = tile.getOrDefault(mapTileNum[x][y],null);
                        if (t!=null){
                            g2.drawImage(t.image,screenX,screenY, gp.tileSize,gp.tileSize,null);


                        }

                    }
                
                
                

            }
        }

    }


}
