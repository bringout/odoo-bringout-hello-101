/** @odoo-module **/

import { Component, useState, onMounted } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class HelloComponent extends Component {
    static template = "hello_component_template";
    
    setup() {
        this.rpc = useService("rpc");
        this.state = useState({
            message: "Loading...",
            isLoading: true,
            userInfo: null,
        });
        
        onMounted(() => {
            this.loadHelloMessage();
        });
    }
    
    async loadHelloMessage() {
        try {
            const result = await this.rpc("/hello_101/hello");
            this.state.message = result.message;
            this.state.userInfo = {
                name: result.user_name,
                company: result.company_name,
                timestamp: result.timestamp,
            };
            this.state.isLoading = false;
        } catch (error) {
            console.error("Failed to load hello message:", error);
            this.state.message = "Bringout says hello!";
            this.state.isLoading = false;
        }
    }
    
    async refreshMessage() {
        this.state.isLoading = true;
        await this.loadHelloMessage();
    }
}

// Register the component as a client action
registry.category("actions").add("hello_dashboard", HelloComponent);
