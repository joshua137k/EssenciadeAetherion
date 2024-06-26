package com.main;

import java.io.File;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;

public class Sound {

    Clip clip;
    File soundURL[] = new File[30];

    public Sound(){
        //0 sound environment
        soundURL[0] = new File("res/soundtrack/music/Red Carpet Wooden Floor.wav");

        //1 gain coin
        soundURL[1] = new File("res/soundtrack/coin.wav");

        //2 powerUp
        soundURL[2] = new File("res/soundtrack/powerup.wav");

        //3 unlock (Door, Chest)
        soundURL[3] = new File("res/soundtrack/unlock.wav");

        //4 fanfarra
        soundURL[4] = new File("res/soundtrack/fanfare.wav");
    }

    public void setFile(int i){
        try {
            AudioInputStream ais = AudioSystem.getAudioInputStream(soundURL[i]);
            clip = AudioSystem.getClip();
            clip.open(ais);

            
        } catch (Exception e) {
        }

    }

    public void play(){
        clip.start();

    }

    public void loop(){
        clip.loop(Clip.LOOP_CONTINUOUSLY);
    }

    public void stop(){
        clip.stop();

    }
    
}
