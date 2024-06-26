package com.data;

public enum UID {

    Arrow("res/objects/0_arrow.png"),
    Key("res/objects/10_key.png"),
    Pickaxe("res/objects/11_pickaxe.png"),
    Scythe("res/objects/12_scythe.png"),
    Shovel("res/objects/13_shovel.png"),
    Waterbucket("res/objects/14_waterBucket.png"),
    Axe("res/objects/1_axe.png"),
    Boot("res/objects/2_boot.png"),
    Bow("res/objects/3_bow.png"),
    Bucket("res/objects/4_bucket.png"),
    Chestclosed("res/objects/5_chestClosed.png"),
    Chestopened("res/objects/6_chestOpened.png"),
    Doorclosed("res/objects/7_doorClosed.png"),
    Dooropened("res/objects/8_doorOpened.png"),
    Fork("res/objects/9_fork.png"),
    Bush("res/tiles/world/15_bush.png"),
    Dirt("res/tiles/world/16_dirt.png"),
    Floor("res/tiles/world/17_floor.png"),
    Grass("res/tiles/world/18_grass.png"),
    Mussstone("res/tiles/world/19_mussStone.png"),
    Sand("res/tiles/world/20_sand.png"),
    Stone("res/tiles/world/21_stone.png"),
    Tree("res/tiles/world/22_tree.png"),
    Water("res/tiles/world/23_water.png");

    private final String path;

    UID(String path) {
        this.path = path;
    }

    public String getPath() {
        return path;
    }

}