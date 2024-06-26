package com.object;

import com.data.UID;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;


public class OBJ_Boot extends SuperObject {

    public OBJ_Boot(){
        name = UID.Boot;
        try {
            image = ImageIO.read( new File(name.getPath()));
            
        } catch (IOException e) {
            e.printStackTrace();
        }
        collision=true;
        
    }
    
}
