function FindProxyForURL(url, host) {

    // use proxy for specific domains
    if (shExpMatch(host, "http://132.231.59.224:*"))
        alert('Proxy triggered: ' + url + host)
        return "PROXY 132.231.59.224:80";

    // by default use no proxy
    return "DIRECT";
}