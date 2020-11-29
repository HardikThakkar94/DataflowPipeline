/*! For license information please see 31.44e936d5.chunk.js.LICENSE.txt */
(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[31],{2279:function(e,t,n){"use strict";n.r(t);var r,o=n(3),a=n(33),i=n(0),c=n.n(i),l=n(240),u=n(227),d=n(115);!function(e){e.ASCENDING="ascending",e.DESCENDING="descending"}(r||(r={}));var s=n(22),h=n.n(s),f=h()("div",{target:"e10os9ge0"})((function(e){var t=e.width,n=e.theme;return{width:t,border:"1px solid ".concat(n.colors.lightestGray),boxSizing:"content-box","& .table-top-right":{overflowX:"hidden",backgroundColor:n.colors.lightestGray},"& .table-bottom-left":{overflowY:"hidden",backgroundColor:n.colors.lightestGray}}}),""),m=h()("div",{target:"e10os9ge1"})((function(e){var t=e.theme;return{padding:t.spacing.sm,fontSize:t.fontSizes.smDefault,fontFamily:t.fonts.mono,textAlign:"right",lineHeight:t.lineHeights.none}}),""),g=function(e){return{backgroundColor:e.colors.lightestGray,color:e.colors.darkGray,zIndex:1}},b=function(e){return{overflow:"hidden",whiteSpace:"nowrap",textOverflow:"ellipsis",lineHeight:e.lineHeights.dataframeCell}},v=h()(m,{target:"e10os9ge2"})((function(e){var t=e.theme;return g(t)}),""),w=h()(m,{target:"e10os9ge3"})((function(e){var t=e.theme;return Object(o.a)(Object(o.a)({userSelect:"none"},g(t)),b(t))}),""),p=h()(m,{target:"e10os9ge4"})((function(e){var t=e.theme;return Object(o.a)(Object(o.a)({userSelect:"none"},g(t)),b(t))}),""),S=h()(m,{target:"e10os9ge5"})((function(e){var t=e.theme;return b(t)}),""),y=h()("div",{target:"e10os9ge6"})((function(e){return{position:"absolute",[e.verticalLocator]:"0px",[e.horizontalLocator]:"0px",width:e.width,height:e.height}}),""),C=h()("div",{target:"e10os9ge7"})((function(e){var t=e.theme;return{fontFamily:t.fonts.mono,color:t.colors.darkGray,fontStyle:"italic",fontSize:t.fontSizes.smDefault,textAlign:"center"}}),""),N=n(89),E=n(5),x=function(e,t,n,r){var o=Object(d.c)(n),a=o.headerRows,i=o.headerCols,c=o.dataRows,l=o.cols,u=o.rows,s=25*a,h=function(e,t,n,r,o,a){var i=e>2?200:400,c=[],l=Array.from(Array(e),(function(e,n){return function(e){for(var n=e.index,o=25,i=0;i<Math.min(t,100);i++){var c=-1;c=i<r?i:t>100?Math.floor(Math.random()*t):i;var l=a(n,c).contents,u=8*(l?l.length:0)+24;u>o&&(o=u)}return o}({index:n})})),u=l.reduce((function(e,t){return e+t}),0),d=o-u;if(d<0)c=l.map((function(e){return e>i?i:e}));else{var s=l.filter((function(e){return e>i})),h=d/s.length;c=l.map((function(e,t){return t in s.keys()?e+h:e}))}var f=c.reduce((function(e,t){return e+t}),0);if(f>o*(2/3)&&f<o){var m=(o-f)/e;c=c.map((function(e){return e+m})),f=c.reduce((function(e,t){return e+t}),0)}var g=Math.min(f,o),b=c.slice(0,n).reduce((function(e,t){return e+t}));return{elementWidth:g,columnWidth:function(e){var t=e.index;return c[t]},headerWidth:b}}(l,u,i,a,t-2,r),f=h.elementWidth,m=h.columnWidth,g=h.headerWidth;if(0===c&&f<60){f=60,g=60;for(var b=0,v=0;v<l;v++)b+=m({index:v});b<60&&(m=function(){return 60/l})}return{rowHeight:25,headerHeight:s,border:2,height:Math.min(25*u,e||300),elementWidth:f,columnWidth:m,headerWidth:g}},D={corner:v,"col-header":w,"row-header":p,data:S};var I=n(65),j=h()(I.b,{target:"ehzvqkj0"})((function(e){var t=e.theme;return{fontSize:t.fontSizes.xs,marginRight:t.spacing.twoXS,opacity:.3,verticalAlign:"top"}}),"");function G(e){var t,n,o,a=e.CellType,i=e.columnIndex,l=e.contents,u=e.rowIndex,d=e.sortedByUser,s=e.style,h=e.columnSortDirection,f=e.headerClickedCallback,m=l,g=h===r.DESCENDING;null!=f&&0===u&&(t=function(){return f(i)},n="button",o=0,m=null==h?'Sort by column "'.concat(l,'"'):'Sorted by column "'.concat(l,'" (').concat(g?"descending":"ascending",")"));var b=0===u?function(e){switch(e){case r.ASCENDING:return c.a.createElement(j,{type:"chevron-top"});case r.DESCENDING:return c.a.createElement(j,{type:"chevron-bottom"});case void 0:default:return null}}(h):void 0;return c.a.createElement(a,{style:s,onClick:t,role:n,tabIndex:o,title:m,"data-testid":a.displayName},d?b:"",l)}var O=Object(u.a)((function(e){var t=e.element,n=e.height,u=e.width,s=c.a.useRef(null),h=Object(i.useState)(!1),m=Object(a.a)(h,2),g=m[0],b=m[1],v=Object(i.useState)(0),w=Object(a.a)(v,2),p=w[0],S=w[1],I=Object(i.useState)(r.ASCENDING),j=Object(a.a)(I,2),O=j[0],R=j[1],k=Object(d.g)(t.get("data")),z=Object(a.a)(k,2)[1],A=Object(d.c)(t),W=A.headerRows,H=A.headerCols,L=A.dataRows,M=A.cols,B=A.rows,F=function(e){var t=r.ASCENDING;p===e&&(t=t!==r.ASCENDING?r.ASCENDING:r.DESCENDING),S(e),R(t),b(!0)},T=function(e){var n=Object(d.c)(t),o=n.headerCols,a=n.dataRows,i=O!==r.DESCENDING;if(p<o||p-o>=e){for(var c=new Array(a),l=0;l<a;l+=1)c[l]=i?l:a-(l+1);return c}return Object(d.d)(t,p-o,i)}(z),J=function(e){var t=e.element,n=e.headerRows,r=e.sortedDataRowIndices;return function(e,o){if(null!=r&&o>=n){var a=o-n;a>=0&&a<r.length?(o=r[a],o+=n):Object(E.d)("Bad sortedDataRowIndices ("+"rowIndex=".concat(o,", ")+"headerRows=".concat(n,", ")+"sortedDataRowIndices.length=".concat(r.length))}var i=Object(d.b)(t,e,o),c=i.contents,l=i.styles,u=i.type;return{Component:D[u],styles:l,contents:Object(N.b)(c)}}}({element:t,headerRows:W,sortedDataRowIndices:T}),U=function(e){return function(t){var n=t.columnIndex,r=t.key,a=t.rowIndex,i=t.style,l=e(n,a),u=l.Component,d=l.styles,s=l.contents,h=0===a?F:void 0,f=n===p?O:void 0,m=Object(o.a)(Object(o.a)({},i),d);return c.a.createElement(G,{key:r,CellType:u,columnIndex:n,rowIndex:a,style:m,contents:s,sortedByUser:g,columnSortDirection:f,headerClickedCallback:h})}}(J),X=x(n,u,t,J),q=X.rowHeight,Y=X.headerHeight,K=X.border,P=X.height,Q=X.elementWidth,V=X.columnWidth,Z=X.headerWidth;return setTimeout((function(){null!=s.current&&s.current.recomputeGridSize()}),0),Object(i.useEffect)((function(){p-H>=z&&(S(0),R(r.ASCENDING),b(!1))}),[p,H,z]),c.a.createElement(f,{width:Q,className:"stDataFrame"},c.a.createElement(l.MultiGrid,{cellRenderer:U,fixedColumnCount:H,fixedRowCount:W,columnWidth:V,columnCount:M,enableFixedColumnScroll:!0,enableFixedRowScroll:!0,height:P,rowHeight:q,rowCount:B,width:Q,classNameBottomLeftGrid:"table-bottom-left",classNameTopRightGrid:"table-top-right",hideBottomLeftGridScrollbar:!0,hideTopRightGridScrollbar:!0,ref:s}),c.a.createElement(y,{verticalLocator:"top",horizontalLocator:"right",width:K,height:Y}),c.a.createElement(y,{verticalLocator:"bottom",horizontalLocator:"left",width:Z,height:K}),0===L?c.a.createElement(C,null,"empty"):null)}));n.d(t,"default",(function(){return O}))}}]);
//# sourceMappingURL=31.44e936d5.chunk.js.map