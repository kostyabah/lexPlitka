var more_btns = document.querySelectorAll('div.card_container .card .card__btn')
var cards = document.querySelectorAll('div.card_container .card')
var text_deeps = document.querySelectorAll('div.card_container .card__content .collapse')

//cards = [].map.call(cards, (item) => new bootstrap.Collapse(item) )
//var collapse_more_btns = [].map.call(more_btns, (item) => new bootstrap.Collapse(item) )
//var collapse_text_deeps = [].map.call(text_deeps, (item) => new bootstrap.Collapse(item), )

var allContent = document.querySelectorAll('.content_for_all');


let stackMind = []
function getOrCreateInstance(el){
  let isCreating = false;
  let currentInstance = null; 
  stackMind.forEach((instance) => {
    if( instance.el === el ){
      currentInstance = instance;
    }else{

    }
  })
  if(!currentInstance){
    currentInstance = {
      el : el,
      addClass(className){
        el.classList.add(className)
      },
      removeClass(className){
        el.classList.remove(className)
      },
      hide(){
        el.classList.add('hide');
        
        //el.classList.add('collapse');
      },
      show(){
        el.classList.remove('hide');
        //el.classList.remove('collapse');
      }
    }
    stackMind.push(currentInstance);
  }
  return currentInstance;
  
}
  
window.addEventListener('load', ()=> {
  var cardsDoms = document.querySelectorAll('div.card_container .card')
  cardsDoms.forEach((card) => getOrCreateInstance(card))
  document.body.addEventListener('click', ()=>{
    allContent[0].classList.remove('collapse');
    allContent[1].classList.remove('collapse');
    cardsDoms.forEach((card, i_card) => {
      //bootstrap.Collapse.getOrCreateInstance
      let instanceCollapse = getOrCreateInstance(card)
      let btn = getOrCreateInstance(card.querySelector('.card__btn'))
      let hideContent = getOrCreateInstance(card.querySelector('.card__content .addons')) 
      instanceCollapse.removeClass('expand-card')
      instanceCollapse.show();
      hideContent.hide();
      btn.show();
      //more_btns[i_card].hide();
    })
  })
  
  
  cardsDoms.forEach((card, i_btn) => {
    console.log(i_btn);

    let btn = card.querySelector('.card__btn')
    let hideContent = card.querySelector('.card__content .addons') 
    let card_collapse = getOrCreateInstance(card)
    card_collapse.btn = btn;
    card_collapse.hideContent = hideContent;
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      allContent[0].classList.add('collapse');
      allContent[1].classList.add('collapse');  
      cardsDoms.forEach((card, i_card) => {
        let instanceCollapse = getOrCreateInstance(card)
        let btn = getOrCreateInstance(
          card.querySelector('.card__btn')
        )
        let hideContent = getOrCreateInstance(
          card.querySelector('.card__content .addons')
        )  
        if(card_collapse !== instanceCollapse){
          instanceCollapse.removeClass('expand-card')
          instanceCollapse.hide()
          hideContent.hide()
          btn.show();
        }else{
          instanceCollapse.addClass('expand-card')
          card_collapse.show();
          hideContent.show()
          btn.hide();
        }
      })
    })
  })
})
   


