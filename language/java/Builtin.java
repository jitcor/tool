public class Builtin {
    @SafeVarargs
    public static <T> T[] append(T[] slice, T... elems){
        Object newElems[]=new Object[slice.length+elems.length];
        System.arraycopy(slice,0,newElems,0,slice.length);
        System.arraycopy(elems,0,newElems,slice.length,elems.length);
        return (T[])newElems;
    }
}
