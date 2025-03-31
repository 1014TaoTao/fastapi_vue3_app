import { request } from '../utils/request';

export function login(data) {
    return request({
        url: '/api/login', 
        method: 'post',
        data: data,
        header: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    });
}

export function forgot_password(data) {
    return request({ 
        url: '/api/forgot_password', 
        method: 'patch',
        data: data
    });
}


export function register(data) {
    return request({
        url: '/api/register',
        method: 'post',
        data: data, 
    })
}

export function logout(data) {
    return request({
        url: '/api/logout', 
        method: 'post',
        data: data, 
    });
}

export function list_user(params) {
    return request({ 
        url: '/api/users', 
        method: 'get',
        data: params 
    });
}

export function create_user(data) {
    return request({ 
        url: '/api/user', 
        method: 'post',
        data: data
    });
}

export function detail_user(id) {
    return request({ 
        url: `/api/user/${id}`,
        method: 'get'
    });
}

export function update_user(id, data) {
    return request({ 
        url: `/api/user/${id}`, 
        method: 'patch', 
        data: data 
    });
}

export function delete_user(id) {
    return request({ 
        url: `/api/user/${id}`, 
        method: 'delete' 
    });
}

export function list_customer(params) {
    return request({ 
        url: '/api/customers', 
        data: params 
    });
}

export function create_customer(data) {
    return request({ 
        url: '/api/customer',
        method: 'post',
        data: data 
    });
}

export function detail_customer(id) {
    return request({ 
        url: `/api/customer/${id}`,
        method: 'get'
    });
}

export function update_customer(id, data) {
    return request({ 
        url: `/api/customer/${id}`, 
        method: 'put', 
        data: data 
    });
}

export function delete_customer(id) {
    return request({ 
        url: `/api/customer/${id}`, 
        method: 'delete' 
    });
}


export function detail_customer_funding(id) {
    return request({ 
        url: `/api/customer/${id}/funding`,
        method: 'get'
    });
}


export function detail_customer_spot(id) {
    return request({ 
        url: `/api/customer/${id}/spot`,
        method: 'get'
    });
}


export function detail_customer_uniaccount(id) {
    return request({ 
        url: `/api/customer/${id}/uniaccount`,
        method: 'get'
    });
}


export function detail_customer_uniaccount_funding(id) {
    return request({ 
        url: `/api/customer/${id}/uniaccount_funding`,
        method: 'get'
    });
}


export function detail_customer_um(id) {
    return request({ 
        url: `/api/customer/${id}/um`,
        method: 'get'
    });
}


export function detail_customer_cm(id) {
    return request({ 
        url: `/api/customer/${id}/cm`,
        method: 'get'
    });
}
