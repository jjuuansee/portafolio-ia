// toc-control.js
// If a page contains an element with id="show-toc", add a body class to re-enable the right TOC
(function(){
  try{
    document.addEventListener('DOMContentLoaded', function(){
      if (document.getElementById('show-toc')){
        document.body.classList.add('show-toc');
      }
      if (document.getElementById('show-sidebar')){
        document.body.classList.add('show-sidebar');
      }
    });
  }catch(e){
    console.warn('toc-control: could not run', e);
  }
})();
