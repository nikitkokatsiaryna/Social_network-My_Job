// export default class extends Stimulus.Controller {
//
//     editImage(event) {
//         let profileId = event.currentTarget.dataset.id;
//
//         $.ajax({
//             type: 'post',
//             url: `/profile/${profileId}/`,
//             success: (response) => {
//                 // debugger
//                 this.getController('modal').element.innerHTML = response
//             },
//             error: (response) => {
//                 // debugger
//             },
//         })
//     }
// }
//
