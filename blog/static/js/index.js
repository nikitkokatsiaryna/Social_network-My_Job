import ExperienceIndex from './controllers/experience/index.js'
import ExperienceNew from './controllers/experience/new.js'

import EducationIndex from './controllers/education/index.js'
import EducationNew from './controllers/education/new.js'

import CertificateIndex from './controllers/certificate/index.js'
import CertificateNew from './controllers/certificate/new.js'

import Modal from './controllers/modal.js'

const application = Stimulus.Application.start()

application.register("experience--index", ExperienceIndex)
application.register("experience--new", ExperienceNew)

application.register("education--index", EducationIndex)
application.register("education--new", EducationNew)

application.register("certificate--index", CertificateIndex)
application.register("certificate--new", CertificateNew)

application.register("modal", Modal)
