export default class extends Stimulus.Controller {

    load() {

        $.ajax({
            type: 'get',
            url: this.element.dataset.url,

            success: (response) => {
                // debugger
                this.element.outerHTML = response
            },
            error: (response) => {
                // debugger
            },
        })
    }


    getController(identifier) {
        const controller = this.application.controllers.find(controller => controller.identifier === identifier);
        if (!controller) throw `Controller '${identifier}' are not registered.`;
        return controller;
    }
}
