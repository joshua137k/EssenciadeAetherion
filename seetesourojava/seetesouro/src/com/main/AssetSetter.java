package com.main;

import com.data.UID;
import com.object.SuperObject;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.function.Supplier;

public class AssetSetter {

    GamePanel gp;
    

    public AssetSetter(GamePanel gp){
        this.gp = gp;
    }

    public void setObject(){
        int index = 0;
        try {
            BufferedReader br = new BufferedReader(new FileReader("res/maps/world01/objects.txt"));
            String line;
            int row = 0;
            while ((line = br.readLine())!=null){
                String[] l = line.split(" ");
                for (int col=0;col<l.length;col++){
                    int id = Integer.parseInt(l[col]);

                    if (id >0){
                        setNewObject(index,id, col*gp.tileSize, row*gp.tileSize);
                        index++;
                    }

                    }
                row++;
            } 
                
            
        } catch (Exception e) {
            e.printStackTrace();
        }
        



    }
    
    public void setNewObject(int index,int id,int x,int y){
        
        UID typeOBJ = gp.typeUID[id];
        
        Supplier<SuperObject> supplier = gp.UIDSuplier.objectSuppliers.get(typeOBJ);
        gp.obj[index] = supplier.get();
        gp.obj[index].worldX = x;
        gp.obj[index].worldY = y;

    }
}
