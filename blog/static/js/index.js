import ExperienceIndex from './controllers/experience/index.js'
import ExperienceNew from './controllers/experience/new.js'
import ExperienceEdit from './controllers/experience/edit.js'

import EducationIndex from './controllers/education/index.js'
import EducationNew from './controllers/education/new.js'
import EducationEdit from './controllers/education/edit.js'

import Modal from './controllers/modal.js'

const application = Stimulus.Application.start()

application.register("experience--index", ExperienceIndex)
application.register("experience--new", ExperienceNew)
// application.register("experience--edit", ExperienceEdit)

application.register("education--index", EducationIndex)
application.register("education--new", EducationNew)
application.register("education--edit", EducationEdit)

application.register("modal", Modal)
