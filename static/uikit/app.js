// Invoke Functions Call on Document Loaded
// document.addEventListener('DOMContentLoaded', function () {
//   hljs.highlightAll();
// });

let alert = document.querySelector('.alert');
let closeBtn = document.querySelector('.alert__close');

closeBtn.addEventListener('click' ,function (){
  alert.remove();
  } )