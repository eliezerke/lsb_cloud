class Theme
{
    constructor() {
        // The parenr widgets 
        this.nav = document.getElementById("navbar");
        this.drawer = document.getElementById("drawer");
        this.content = document.getElementById('main');
        this.left_pane = document.getElementById("leftpane");
        this.right_pane = document.getElementById("rightpane");
        this.contentbox = document.getElementById("contentbox");
        this.footer = document.getElementById("footer");
        this.footer_content = document.getElementById("footercontent");
        this.backed = document.getElementById("backed");
        this.body = document.body;

        // Children of the parents above
        this.pri_buttons = document.getElementsByClassName("btn-primary");
        this.sec_buttons = document.getElementsByClassName("btn-secondary");
        this.btn_link = document.getElementsByClassName("btn-link");

        // other general widgets and components => text, buttons etc
        this.foot_text = document.getElementById("footercontent");
        // AOW => any other widget
    }

    light(state) {
        // Background colors and images
        this.body.style.backgroundColor = "rgb(240, 240, 240)";
        this.nav.style.backgroundColor = "#e0e0e0";
        this.right_pane.style.backgroundImage = "linear-gradient(to right,rgba(230, 230, 230, 0.9),rgba(209, 209, 209, 0.79))";
        this.left_pane.style.backgroundImage = "linear-gradient(to right,rgba(255, 255, 255, 0.9),rgba(187, 187, 187, 0.79))";
        this.backed.style.backgroundImage = "url(/assets/img/picture1_dark.png)"
        this.footer.style.backgroundColor = "rgb(216, 216, 216)";
        
        
        // font-colors and stuff
        this.contentbox.style.color = "rgb(24, 24, 24)";
        this.foot_text.classList.add("dark-text");
        this.body.style.color = "#222222";

    }
    dark(state) {
        // Background colors and images
        this.body.style.backgroundColor = "rgb(31, 31, 31)";
        this.nav.style.backgroundColor = "#565656";
        this.right_pane.style.backgroundImage = "linear-gradient(to right,rgba(26, 26, 26, 0.904),rgba(58, 58, 58, 0.788))";
        this.left_pane.style.backgroundImage = "linear-gradient(to right,rgba(26, 26, 26, 0.904),rgba(58, 58, 58, 0.788))";
        this.backed.style.backgroundImage = "url(/assets/img/picture1_dark.png)"
        this.footer.style.backgroundColor = "rgb(63,63,63)";
        
        
        // font-colors and stuff
        this.contentbox.style.color = "rgb(255, 255, 255)";
        this.foot_text.classList.add("dark-text");
        this.body.style.color = "#ffffff";

    }
}

// Instanciating our objects for use
toggle = new Theme();