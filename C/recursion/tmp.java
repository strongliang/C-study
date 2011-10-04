interface State {
    int cleanUp() {}
    int addSubs() {} 
    int addFlows(){}
}

class Normal {
    int cleanUp() {
        //nothing;
    }

    int addSubs() {
        //add subs
    }

    int addFlows(){
    }
}


class MOL1 {
    int cleanUp() {
        //nothing;
    }

    int addSubs() {
        //can't add subs;
    }

    int addFlows(){
        //add flows
    }
}

class MOL2 {
    int cleanUp() {
        //cleanUp flows
    }

    int addSubs() {
        //can't add subs
    }

    int addFlows(){
        //can't add flows
    }
}

class MOL3 {
    int cleanUp() {
        //release memory
        //cleanup flows
    }

    int addSubs() {
        //can't add subs
    }

    int addFlows(){
        //can't add flows
    }
}

