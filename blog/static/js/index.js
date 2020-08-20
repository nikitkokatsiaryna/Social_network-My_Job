import ExperienceIndex from './controllers/experience/index.js'
import ExperienceNew from './controllers/experience/new.js'
import ExperienceEdit from './controllers/experience/edit.js'
import Modal from './controllers/modal.js'

const application = Stimulus.Application.start()

application.register("experience--index", ExperienceIndex)
application.register("experience--new", ExperienceNew)
application.register("experience--edit", ExperienceEdit)
application.register("modal", Modal)
