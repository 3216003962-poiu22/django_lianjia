window.onload = function(){
    var a = window.location.pathname;
	var reg = /(?:\/([A-Za-z]+))?(?:\/([\_A-Za-z]+))?/;
	var res = a.match(reg);
	var oSidewrap = document.querySelector('.side-wrap');
	var oBg = document.querySelector('.side-wrap .side-bg');
	var oContent = document.querySelector('.side-wrap .side-content');
	var oContentList = document.querySelector('.side-wrap .side-content .side-list');
	var oContentListchild = document.querySelectorAll('.side-wrap .side-content .side-list li');
	var oContentListchildTag = document.querySelectorAll('.side-wrap .side-content .side-list li a');
	var oSpan = document.querySelector('.side-wrap .side-bg .side-mask span');
	adjust();
	on();
	over();
	scroll();
	way();
	function on(){
		oBg.onmouseover = function(){
			oSpan.childNodes[0].className = "fa fa-eye";
			oBg.style.transform = 'translateX(60px)';
			setTimeout(function(){
				oContent.style.transform = 'translateX(0px)';
				oContent.classList.add('shadow')
			},300)
			oContent.addEventListener('transitionend',function(){
				oContent.classList.add('shadow');
			})
		}
	}

	function over(){
		oContent.onmouseleave = function(e){
			oSpan.childNodes[0].className = "fa fa-list-ul";
			oBg.style.transtionDelay = '0';
			oBg.style.transform = 'translateX(0px)';
			oContent.style.transform = 'translateX(200px)';
			oContent.addEventListener('transitionend',function(){
				oContent.classList.remove('shadow');
			})
		}

	}
	
	function adjust(){
		oBg.style.height = window.innerHeight+'px';
		oContent.style.height = window.innerHeight+'px';
		window.onresize = function(){
			oBg.style.height = window.innerHeight+'px';
			oContent.style.height = window.innerHeight+'px';
		}
	}

	function scroll(){
		window.onscroll = function(){
			console.log(document.documentElement.scrollTop )
			oSidewrap.style.top = document.documentElement.scrollTop  + 'px';
		}
	}

	function way(){
		switch(res[2]){
		    case 'number_count':
		        oContentListchild[1].style.transform = 'scale(1.2)';
		        oContentListchild[1].style.fontWeight= 'bolder';
		        break;
            case 'unit_total_table':
                oContentListchild[2].style.transform = 'scale(1.2)';
		        oContentListchild[2].style.fontWeight= 'bolder';
		        break;
            case 'region_price':
                oContentListchild[3].style.transform = 'scale(1.2)';
		        oContentListchild[3].style.fontWeight= 'bolder';
		        break;
            case 'layout_type':
                oContentListchild[4].style.transform = 'scale(1.2)';
		        oContentListchild[4].style.fontWeight= 'bolder';
		        break;
		}
	}
    whathref();
	function whathref(){
        oContentListchildTag[1].href = '/'+ res[1] +'/number_count';
        oContentListchildTag[2].href = '/'+ res[1] +'/unit_total_table';
        oContentListchildTag[3].href = '/'+ res[1] +'/region_price';
        oContentListchildTag[4].href = '/'+ res[1] +'/layout_type';

	}
}