import { useUserStore } from "../stores/index";

export function request(options) {
    const userStore = useUserStore();
    uni.showToast({
        title: "加载中...",
        icon: "loading",
        mask: true,
    });

    return new Promise((resolve, reject) => {
        uni.request({
            url: import.meta.env.VITE_API_BASE_URL + options.url,
            method: options.method || "GET",
            data: options.data || "",
            header: {
                Authorization: userStore.token ? `Bearer ${userStore.token}` : "",
                ...(options.header || {}),
            },
            timeout: import.meta.env.VITE_TIMEOUT,
            success: (res) => {
                if (res.data.code === 200) {
                    uni.showToast({
                        title: res.data.message,
                        icon: "success",
                        mask: true,
                    });
                    
                    resolve(res.data);
                } else if (res.data.code === 401) {
                    uni.showToast({
                        title: res.data.message || "未登录",
                        icon: "none",
                        mask: true,
                    });
                    userStore.clearUser();
                    uni.reLaunch({ url: "/pages/login/login" });
                    reject(res.data);
                } else {
                    uni.showToast({
                        title: res.data.message || "请求发生异常",
                        icon: "none",
                        mask: true,
                    });
                    reject(res.data);
                }
            },
            fail: (error) => {
                uni.showToast({
                    title: "请求异常",
                    icon: "none",
                    mask: true,
                });
                reject(error);
            }
        });
    });
}