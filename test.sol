pragma solidity ^0.4.24;

contract TestContract {
    mapping(address=>bytes) infos;
    address[] schools;//需要提前写进去合约学校的地址
    uint refreshTime;

    // event
    event DownloadInfoEvent(address school_addr)
    event UpdateInfoEvent(address school_addr, bytes info);
    
    constructor() public {
        refreshTime = now + 1 days;
    }

    function updateInfo() public {
        infos[msg.sender] = msg.data;
        emit UpdateInfoEvent(msg.sender, msg.data);
    }

    function downloadInfo() public {
        bytes[] data;
        //只返回已经加入合约的学校上传的信息
        for (uint i = 0; i<schools.length; i++) {
            school_addr = schools[i];
            data.push(infos[school_addr]);
        }
        emit DownloadInfoEvent(msg.sender);
        return data;
    }

    function refresh() public {
        //24h 后清空之前的信息
        require(now > refreshTime);
        infos = mapping(address=>bytes);
    }