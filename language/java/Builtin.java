public class Builtin {
    public static byte[] append(byte[] slice, byte... elems){
        byte[] newElems =new byte[slice.length+elems.length];
        System.arraycopy(slice,0,newElems,0,slice.length);
        System.arraycopy(elems,0,newElems,slice.length,elems.length);
        return newElems;
    }

}
