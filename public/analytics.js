// Googleアナリティクス（GA4）。測定ID（G-で始まる番号）を受け取ったら GA_ID に入れる。
// 'G-XXXXXXXXXX' のままの間は、何も送らない。
const GA_ID = 'G-968VQMM06X';

window.dataLayer = window.dataLayer || [];
window.gtag = function () { window.dataLayer.push(arguments); };

if (/^G-[A-Z0-9]{6,}$/.test(GA_ID) && GA_ID !== 'G-XXXXXXXXXX') {
  const s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
  document.head.appendChild(s);
  window.gtag('js', new Date());
  window.gtag('config', GA_ID);
}
