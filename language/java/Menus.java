
import java.util.*;

public class Menus {
    public static final boolean DEBUG = true;

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
        private MenuOption menuOptionBack=new MenuOption("back to previous","",new MenuAction(){
            @Override
            public void doAction() {
                if(Menu.this.parentMenu!=null){
                    Menu.this.parentMenu.show();
                }
            }
        });

        public Menu(Menu parent) {
            this.parentMenu = parent;
            if(this.parentMenu==null){
                menuOptionBack=menuOptionExit;
            }
        }

        public void addOptions(MenuOption... options) {
            for (MenuOption option : options) {
                if (ids.add(option.name)) {
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
            return this.options;
        }
        public Menu setMenuOptionBack(MenuOption menuOptionBack){
            if(menuOptionBack==null)throw new IllegalArgumentException("menuOptionBack not support reset null");
            this.menuOptionBack=menuOptionBack;
            return this;
        }

        public void show() {
            int i = 1;
            Map<Integer, MenuOption> optionMap = new HashMap<>();
            this.options.sort(Collections.reverseOrder());
            for (MenuOption option : this.options) {
                if (!option.show) continue;
                System.out.println(buildOptionText(i,option));
                optionMap.put(i, option);
                i++;
            }
            System.out.println(buildOptionText(i,this.menuOptionBack));
            try {
                System.out.print(getInputPrefix());
                Scanner scanner = new Scanner(System.in);
                if (scanner.hasNext()) {
                    int index = scanner.nextInt();
                    if (index == i) {
                        if (this.parentMenu != null) {
                            this.parentMenu.show();
                        } else {
                            System.exit(0);
                        }

                    } else {
                        optionMap.get(index).doAction();
                        show();
                    }
                }
            } catch (Exception e) {
                if (DEBUG) {
                    e.printStackTrace();
                }
                show();
            }
        }
        protected String buildOptionText(int i,MenuOption option){
            return String.format("%d) %s  %s", i, option.name, option.summary);
        }
        protected String getInputPrefix(){
            return "option >";
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
/*demo

private static void printMenu() {
        Menus.Menu rootMenu = new Menus.Menu( null);
        Menus.Menu getPropMenu = new Menus.Menu( rootMenu);
        getPropMenu.addOptions(new Menus.MenuOption( "get adb debug", "get adb debug", new Menus.MenuAction() {
            @Override
            public void doAction() {
                System.out.println("todo get adb debug prop");
            }
        }));
        rootMenu.addOptions(new Menus.MenuOption("sign apk", "sign apk", new Menus.MenuAction() {
                    @Override
                    public void doAction() {
                        System.out.println("todo sign apk");
                    }
                }),
                new Menus.MenuOption("read apk path", "read apk path with adb command", new Menus.MenuAction() {
                    @Override
                    public void doAction() {
                        System.out.println("todo apk path");
                    }
                }),
                new Menus.MenuOption( "check apk", "check apk info", new Menus.MenuAction() {
                    @Override
                    public void doAction() {
                        System.out.println("todo check apk info");
                    }
                })
        );
        rootMenu.addOptions(new Menus.MenuOption( "get prop", "get device prop with adb", new Menus.MenuAction() {
            @Override
            public void doAction() {
                getPropMenu.show();
            }
        }));
        rootMenu.show();
    }

*/
