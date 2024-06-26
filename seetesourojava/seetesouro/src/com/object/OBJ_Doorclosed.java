package com.object;

import com.data.UID;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;


public class OBJ_Doorclosed extends SuperObject {

    public BufferedImage imageOpen;

    public OBJ_Doorclosed(){
        name = UID.Doorclosed;
        try {
            image = ImageIO.read( new File(name.getPath()));
            imageOpen = ImageIO.read( new File(UID.Dooropened.getPath()));
            
        } catch (IOException e) {
            e.printStackTrace();
        }
        collision=true;

        
    }
    
}
