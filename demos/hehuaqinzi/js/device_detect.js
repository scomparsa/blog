/**
 * Device detect
 **/

'use strict';

window.onload = function() {
  var ua = navigator.userAgent.toLowerCase(),
    device = (/android/.test(ua)) ? 'android': 'ios', // Default device: iOS
    appLink = APP_LINK_MAP[device],
    appDownloadBtnEl = document.getElementById('app-download-btn');
  
  appDownloadBtnEl.setAttribute('href', appLink);
};