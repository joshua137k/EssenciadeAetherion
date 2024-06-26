
package com.data;


import com.object.*;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Supplier;


public class Suplier {

    public Map<UID, Supplier<SuperObject>> objectSuppliers;

    public Suplier(){
        objectSuppliers = new HashMap<>();
        objectSuppliers.put(UID.Arrow, OBJ_Arrow::new);
        objectSuppliers.put(UID.Key, OBJ_Key::new);
        objectSuppliers.put(UID.Pickaxe, OBJ_Pickaxe::new);
        objectSuppliers.put(UID.Scythe, OBJ_Scythe::new);
        objectSuppliers.put(UID.Shovel, OBJ_Shovel::new);
        objectSuppliers.put(UID.Waterbucket, OBJ_Waterbucket::new);
        objectSuppliers.put(UID.Axe, OBJ_Axe::new);
        objectSuppliers.put(UID.Boot, OBJ_Boot::new);
        objectSuppliers.put(UID.Bow, OBJ_Bow::new);
        objectSuppliers.put(UID.Bucket, OBJ_Bucket::new);
        objectSuppliers.put(UID.Chestclosed, OBJ_Chestclosed::new);
        objectSuppliers.put(UID.Doorclosed, OBJ_Doorclosed::new);
        objectSuppliers.put(UID.Fork, OBJ_Fork::new);

    }
                
}
