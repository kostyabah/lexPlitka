let slider = document.querySelector('.slider .list');
let items = document.querySelectorAll('.slider .list .item');
let next = document.getElementById('next');
let prev = document.getElementById('prev');
let dots = document.querySelectorAll('.slider .dots li');

let lengthItems = items.length - 1;
let active = 0;





function nextSide(){
    active = active + 1 <= lengthItems ? active + 1 : 0;
    reloadSlider();
}
next.onclick = nextSide;
function prevSide(){
    active = active - 1 >= 0 ? active - 1 : lengthItems;
    reloadSlider();
}
prev.onclick = prevSide;
isAutoSlide = true;
let refreshInterval = setInterval(()=> {
    if(isAutoSlide){
        next.click()
    }
    
}, 3000);
function reloadSlider(){
    //slider.style.marginLeft = -items[active].offsetLeft + 'px';
    let swipeOffset = endTouchX - startTouchX
    //slider.style.marginLeft = 
    let translateHorizontal = swipeOffset - items[active].offsetWidth * active + 'px';
    slider.style.transform = 'translateX('+ translateHorizontal +')'
    let last_active_dot = document.querySelector('.slider .dots li.active');
    if(last_active_dot !== dots[active]){
        last_active_dot.classList.remove('active');
        dots[active].classList.add('active');
    }
    

    clearInterval(refreshInterval);
    refreshInterval = setInterval(()=> {

        if(isAutoSlide){
            next.click()
        }
    }, 3000);


}
let startTouchX = 0; 
let endTouchX = 0;



slider.addEventListener('touchstart', (event) => {
    event.preventDefault();
    slider.style.transitionDuration = '0s'
    isAutoSlide = false;
    startTouchX = event.changedTouches[0].pageX;
    endTouchX = startTouchX;
}, {capture: false, passive: false})

slider.addEventListener('touchmove', (event) => {
    event.preventDefault();
    endTouchX = event.changedTouches[0].pageX;
    reloadSlider();
}, {capture: false, passive: false})

let waitFinishTouchEnd;
slider.addEventListener('touchend', (event) => {
    event.preventDefault();
    slider.classList.remove('transition-wild')
    slider.style.transitionDuration = '0.5s'
    endTouchX = event.changedTouches[0].pageX;
    let swipeOffset = endTouchX - startTouchX;  
    endTouchX  = 0 
    startTouchX = 0
    if( Math.abs(swipeOffset) > 20){
        if( swipeOffset < 0){
            nextSide();
        
        }
        if( swipeOffset > 0){
            prevSide();
            
        }
    }
    
    clearTimeout(waitFinishTouchEnd);
    waitFinishTouchEnd = setTimeout(() => {
        slider.style.transitionDuration = '1s'
        isAutoSlide = true;
    }, 5000)
}, {capture: false, passive: false})

dots.forEach((li, key) => {
    li.addEventListener('click', ()=>{
         active = key;
         reloadSlider();
    })
})
window.onresize = function(event) {
    reloadSlider();
};


// const navLinkEls = document.querySelectorAll('.nav-list-link');


// navLinkEls.forEach(navLinkEl => {
//     navLinkEl.addEventListener('click', function() {
//         document.querySelector('.active')?.classList.remove('active');
//         this.classList.add('active');
//     });
// });



