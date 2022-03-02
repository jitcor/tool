
import java.util.*;

public class Menus {
    public static final boolean DEBUG = false;

    //menu header
    //menu color
    //menu options,priority
    //menu exit,break,continue
    //menu action
//    private static final Map<Integer,Menu> menuMap=new HashMap<>();
//    private static final Map<Integer,MenuOption> optionMap=new HashMap<>();
//    public static Menu obtain(int menuId,Menu parent,MenuOption... options){
//        if(menuMap.containsKey(menuId))return menuMap.get(menuId);
//        menuMap.put(menuId,new Menu(menuId,parent,options));
//        return menuMap.get(menuId);
//    }
//    public static Menu obtain(int menuId,int parentId,MenuOption... options){
//        if(menuMap.containsKey(menuId))return menuMap.get(menuId);
//        menuMap.put(menuId,new Menu(menuId,parentId,options));
//        return menuMap.get(menuId);
//    }
//    public static MenuOption obtain(int id,String title,String summary,MenuAction action,int priority){
//        if(optionMap.containsKey(id))return optionMap.get(id);
//        optionMap.put(id,new MenuOption(id,title,summary,action,priority));
//        return optionMap.get(id);
//    }
//    public static MenuOption obtain(int id,String title,String summary,MenuAction action){
//        return obtain(id,title,summary,action,0);
//    }
    private static final MenuOption menuOptionExit=new MenuOption("exit","",new MenuAction(){
        @Override
        public void doAction() {
            System.exit(0);
        }
    });
    public static class Menu {
        private final List<MenuOption> options = new ArrayList<>();
        private final Menu parentMenu;
        private final Set<String> ids = new HashSet<>();
        private final MenuOption menuOptionBack=new MenuOption("..","",new MenuAction(){
            @Override
            public void doAction() {
                if(Menu.this.parentMenu!=null){
                    Menu.this.parentMenu.show();
                }
            }
        });

        public Menu(Menu parent) {
            this.parentMenu = parent;
        }

        public void addOptions(MenuOption... options) {
            for (MenuOption option : options) {
                if (ids.add(option.name)) {
                    if(option.name.length()>getMaxTitleLength())throw new IllegalArgumentException("Option title max length is "+getMaxTitleLength());
                    this.options.add(option);
                }
            }
        }

        public MenuOption findOptionByName(String name) {
            for (MenuOption option : this.options) {
                if (option.name.equals(name)) {
                    return option;
                }
            }
            return null;
        }
        public List<MenuOption> getAllOption(){
            return new ArrayList<>(this.options);
        }
        public void clearOptions(){
            this.options.clear();
            this.ids.clear();
        }

        public void show() {
            int i = 1;
            Map<Integer, MenuOption> optionMap = new HashMap<>();
            if(this.parentMenu!=null){
                System.out.println(buildOptionText(i,this.menuOptionBack));
                optionMap.put(i++, this.menuOptionBack);
            }
            this.options.sort(Collections.reverseOrder());
            for (MenuOption option : this.options) {
                if (!option.show) continue;
                System.out.println(buildOptionText(i,option));
                optionMap.put(i++, option);
            }
            System.out.println(buildOptionText(i,menuOptionExit));
            optionMap.put(i,menuOptionExit);
            try {
                System.out.print(getInputPrefix());
                Scanner scanner = new Scanner(System.in);
                if (scanner.hasNext()) {
                    int index = scanner.nextInt();
                    if(index>=1&&index<=i){
                        optionMap.get(index).doAction();
                        if(index!=i){
                            show();
                        }
                    }else {
                        System.out.println("warn: please input number 1~"+i);
                        show();
                    }

                }
            } catch (Exception e) {
                if (DEBUG) {
                    e.printStackTrace();
                }
                System.out.println("warn: please input number 1~"+i);
                show();
            }
        }
        protected String buildOptionText(int i,MenuOption option){
            return String.format("%d) %-24s  %s", i, option.name, option.summary);
        }
        protected String getInputPrefix(){
            return "option >";
        }
        protected int getMaxTitleLength(){
            return 20;
        }
    }

    public static class MenuHeader { /*todo*/
    }

    public static class MenuColor { /*todo*/
    }

    public static class MenuOption implements Comparable<MenuOption> {
        private final String name;
        private final String summary;
        private boolean show;
        private MenuAction action;
        private final int priority;

        public MenuOption(String title, String summary, MenuAction action, int priority, boolean show) {
            this.name = title;
            this.summary = summary;
            this.action = action;
            this.priority = priority;
            this.show = show;
        }

        public MenuOption(String title, String summary, MenuAction action, int priority) {
            this(title, summary, action, priority, true);
        }

        public MenuOption(String title, String summary, MenuAction action) {
            this(title, summary, action, 0);
        }

        public void doAction() {
            if (this.action != null) {
                this.action.doAction();
            }
        }

        public MenuOption setShow(boolean isShow) {
            this.show = isShow;
            return this;
        }

        public MenuOption setAction(MenuAction action) {
            this.action = action;
            return this;
        }

        @Override
        public int compareTo(MenuOption o) {
            return this.priority - o.priority;
        }
    }

    public static class MenuAction {
        public void doAction() {
            System.out.println("This is a default action!");
        }
    }

}
