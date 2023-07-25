// Get HTML elements
const burgerMenu = document.getElementById("burger-menu");
const burgerBtn = document.getElementById("burg-btn");
const burgerCloseBtn = document.getElementById("burg-btn-close");
const windowOuterWidth = window.outerWidth;
const popupBlock = document.querySelector(".popups");
const contactsBlock = document.querySelector(".contacts_block");
const aboutUsBlock = document.querySelector(".aboutus_block");
const contactsBtn = document.querySelector("#Contacts");
const deliveryBtn = document.querySelector("#delivery-buy");
const aboutUsBtn = document.querySelector("#AboutUs");
const cartBtn = document.querySelector(".cart_btn");
const cartWrapper = document.querySelector(".cart_wrapper");
const cartBlock = document.querySelector(".cart_block");








// Burger menu dynamic
burgerBtn.addEventListener("click", function() {
    burgerMenu.style.display = "flex";
    burgerCloseBtn.style.display = "block";
    burgerBtn.style.display = "none";
});

burgerCloseBtn.addEventListener("click", function() {
    burgerMenu.style.display = "none";
    burgerBtn.style.display = "flex";
    burgerCloseBtn.style.display = "none";
});

window.addEventListener('resize', function(){
    let w = document.documentElement.clientWidth;
    let h =  document.documentElement.clientHeight;

    if (w > 912){
        burgerBtn.style.display = "none";
        burgerCloseBtn.style.display = "none";
        burgerMenu.style.display = "none";
    }
    else if (w < 912 && $('#burg-btn-close').css('display') == "block"){
        burgerBtn.style.display = "none";
    }
    else if (w < 912 && $('#burg-btn-close').css('display') == "none"){
        burgerBtn.style.display = "flex";
    }
});

// Popup dynamic

const contactsPopUp = document.querySelector(".contactsPopUp-wrapper")
const deliveryPopUp = document.querySelector(".deliveryPopUp-wrapper")
const aboutusPopUp = document.querySelector(".aboutusPopUp-wrapper")



const popup_item = document.querySelectorAll(".popup_item")
var body = document.getElementsByTagName('body')[0];
contactsBtn.addEventListener("click", () => {
    contactsPopUp.classList.remove("popUphidden")
    contactsPopUp.classList.add("popUpshown")


    body.style.overflow = 'hidden';
   
    document.body.scrollTop = 0; // Для Safari
    document.documentElement.scrollTop = 0; // Для Chrome, Firefox, IE and Opera
  
})


deliveryBtn.addEventListener("click", () => {
    deliveryPopUp.classList.remove("popUphidden")
    deliveryPopUp.classList.add("popUpshown")


    body.style.overflow = 'hidden';
   
    document.body.scrollTop = 0; // Для Safari
    document.documentElement.scrollTop = 0; // Для Chrome, Firefox, IE and Opera
  
})



contactsPopUp.addEventListener("click", (e) => {

    if (!e.target.closest(".contactsPopUp-block")) {
    contactsPopUp.classList.remove("popUpshown")
    contactsPopUp.classList.add("popUphidden")

    body.style.overflow = 'visible';
    }
})



deliveryPopUp.addEventListener("click", (e) => {
    if (!e.target.closest(".deliveryPopUp-block")) {
    deliveryPopUp.classList.remove("popUpshown")
    deliveryPopUp.classList.add("popUphidden")

    body.style.overflow = 'visible';
    }
})

aboutUsBtn.addEventListener("click", () => {
    
    aboutusPopUp.classList.remove("popUphidden")
    aboutusPopUp.classList.add("popUpshown")
    document.body.scrollTop = 0; // Для Safari
    document.documentElement.scrollTop = 0; // Для Chrome, Firefox, IE and Opera
    body.style.overflow = 'hidden';
   
   
})

aboutusPopUp.addEventListener("click", (e) => {
    if (!e.target.closest(".aboutusPopUp-block")) {
    aboutusPopUp.classList.remove("popUpshown")
    aboutusPopUp.classList.add("popUphidden")
    body.style.overflow = 'visible';
    }
})

contactsPopUp.addEventListener("mouseover", (e) => {
    if (!e.target.closest(".contactsPopUp-block")) {
        contactsPopUp.classList.add("popUpHover")
    }
    if (e.target.closest(".contactsPopUp-block")) {
        contactsPopUp.classList.remove("popUpHover")
    }
});

aboutusPopUp.addEventListener("mouseover", (e) => {
    if (!e.target.closest(".aboutusPopUp-block")) {
        aboutusPopUp.classList.add("popUpHover")
    }
    if (e.target.closest(".aboutusPopUp-block")) {
        aboutusPopUp.classList.remove("popUpHover")
    }
});

deliveryPopUp.addEventListener("mouseover", (e) => {
    if (!e.target.closest(".deliveryPopUp-block")) {
        deliveryPopUp.classList.add("popUpHover")
    }
    if (e.target.closest(".deliveryPopUp-block")) {
        deliveryPopUp.classList.remove("popUpHover")
    }
});


function removeObjectAndShiftIds(arr, idToRemove) {
    
    const indexToRemove = arr.findIndex(obj => obj.id === idToRemove);
    

    arr.splice(indexToRemove, 1);
    
 
    for (let i = indexToRemove; i < arr.length; i++) {
      arr[i].id = i;
    }
    
    return arr;
  }
// Basket dynamic

let renderCart = () => {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    const cartBody = document.querySelector("ul.cart_item_list");
    cartBody.innerHTML = "";
    cart.forEach(element => {
        const div = document.createElement("div");
        div.setAttribute("id", element["id"]);
        div.innerHTML = `
        <hr class = "hr-basket" id="hr-${element["id"]}">
            <li class="cart_item">
                <div><img class="cart_ProductImg" src=${element["img"]}></div>
                <div class="cart_ProductName">${element["name"]}</div>
                <div class="cart_ProductPrice" id="cart_item-price">${parseInt(element["price"]) * parseInt(element["quantity"])}p.</div>
                <button class="minusBasket" >-</button>
                <div class="countBasket"> ${parseInt(element["quantity"])} </div>
                <button class="plussBasket" >+</button>
                <div class="cart_ProductDeletBtn"> X </div>
            </li>
            
        `;
        cartBody.appendChild(div);
    });
    const totalPriceContent = document.querySelector(".total_price_content");
    const itemsPrices = document.querySelectorAll("#cart_item-price");
    let sum = 0;
    const cropStr = str => str.replace(/\D+/g, '');
    itemsPrices.forEach(e => {
        sum += Number(parseInt(`${e.innerHTML}`));
    });
    totalPriceContent.innerText = `Сумма: ${sum} p.`;



    //увеличение корзины по +
    let plussBasket = document.querySelectorAll(".plussBasket");
    plussBasket.forEach((e, i) => {
      e.addEventListener("click", (event) => {
        event.stopPropagation();
    
        let cart = JSON.parse(localStorage.getItem('cart')) || [];
    
        cart[i].quantity = Number(cart[i].quantity) + 1; // Увеличиваем значение quantity
    
        localStorage.setItem('cart', JSON.stringify(cart));
    
        renderCart();
    
        let totalQuantity = cart.reduce((total, item) => total + Number(item.quantity), 0); // Вычисляем общее количество товаров в корзине
    
        document.querySelector('.basket-check-warp').style.display = 'block';
        document.querySelector('.basket-check').innerText = totalQuantity;
    
        console.log(cart);
      });
    });



    let minusBasket = document.querySelectorAll(".minusBasket");
    minusBasket.forEach((e, i) => {
      e.addEventListener("click", (event) => {
        event.stopPropagation();
    
        let cart = JSON.parse(localStorage.getItem('cart')) || [];
        
        if (Number(cart[i].quantity) > 1){
        cart[i].quantity = Number(cart[i].quantity) - 1; // Увеличиваем значение quantity
    
        localStorage.setItem('cart', JSON.stringify(cart));
    
        renderCart();
    
        let totalQuantity = cart.reduce((total, item) => total + Number(item.quantity), 0); // Вычисляем общее количество товаров в корзине
    
        document.querySelector('.basket-check-warp').style.display = 'block';
        document.querySelector('.basket-check').innerText = totalQuantity;
    
        console.log(cart);
    }
    
      });
    });
    
    

    let cartProductDeletBtn = document.querySelectorAll(".cart_ProductDeletBtn")
    cartProductDeletBtn.forEach((e, i) => {
     
        e.addEventListener("click", (event) => {
            event.stopPropagation()
            let cart = JSON.parse(localStorage.getItem('cart')) || [];
            let count_quantity = 0
            
           
            removeObjectAndShiftIds(cart, i)
            for(j=0; j<cart.length; j++){
                count_quantity += Number(cart[j]['quantity'])
                console.log(cart[j]['quantity'])
            }

            localStorage.setItem('cart', JSON.stringify(cart));
            renderCart()
            if (cart.length > 0){
                document.querySelector('.basket-check-warp').style.display = 'block';
                document.querySelector('.basket-check').innerText = count_quantity
              }
            else if (cart.length === 0){
                document.querySelector('.basket-check-warp').style.display = 'none'
            }
        })
        
    })
}

cartBtn.addEventListener("click", () => {
    cartWrapper.classList.remove("hidden")
    cartWrapper.classList.add("shown")
    document.querySelector("body").style.overflow = "hidden"
    document.body.scrollTop = 0; // Для Safari
    document.documentElement.scrollTop = 0; // Для Chrome, Firefox, IE and Opera
    renderCart()
    
});

cartWrapper.addEventListener("mouseover", (e) => {
    if (!e.target.closest(".cart_block")) {
        cartWrapper.classList.add("hover")
    }
    if (e.target.closest(".cart_block")) {
        cartWrapper.classList.remove("hover")
    }
});
cartWrapper.addEventListener("click", (e) => {
    if (!e.target.closest(".cart_block")) {
        cartWrapper.classList.remove("shown")
        cartWrapper.classList.add("hidden")
       
        body.style.overflow = 'visible';
    }
});











