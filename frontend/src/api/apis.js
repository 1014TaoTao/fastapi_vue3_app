import { request } from "../utils/request";

const contentTypes = {
    form: "application/x-www-form-urlencoded",
    json: "application/json",
    multipart: "multipart/form-data"
};

export function upload(file) {
    return request({
        url: "/api/upload",
        method: "put",
        data: file,
        header: { "Content-Type": contentTypes.multipart }
    });
}

export function login(data) {
    return request({
        url: "/api/login",
        method: "post",
        data,
        header: { "Content-Type": contentTypes.form }
    });
}

export function forgot_password(data) {
    return request({
        url: "/api/forgot_password",
        method: "patch",
        data: data
    });
}

export function register(data) {
    return request({
        url: "/api/register",
        method: "post",
        data: data
    });
}

export function logout(data) {
    return request({
        url: "/api/logout",
        method: "post",
        data: data
    });
}

export function list_user(params) {
    return request({
        url: "/api/users",
        method: "get",
        data: params,
        loading: params?.noLoading ? false : true
    });
}

export function create_user(data) {
    return request({
        url: "/api/user",
        method: "post",
        data: data
    });
}

export function detail_user(id) {
    return request({
        url: `/api/user/${id}`,
        method: "get"
    });
}

export function update_user(id, data) {
    return request({
        url: `/api/user/${id}`,
        method: "patch",
        data: data
    });
}

export function delete_user(id) {
    return request({
        url: `/api/user/${id}`,
        method: "delete"
    });
}
