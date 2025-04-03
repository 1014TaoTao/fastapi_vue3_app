import { useUserStore } from '../stores/index'

export function request(options) {
    const userStore = useUserStore()
    
    return new Promise((resolve, reject) => {
        uni.request({
            url: import.meta.env.VITE_API_BASE_URL + options.url,
            method: options.method || "GET",
            data: options.data || "",
            header: {
                'Authorization': userStore.token ? `Bearer ${userStore.token}` : '',
                ...options.header || {}
            },
            timeout: import.meta.env.VITE_TIMEOUT,
            success: (res) => {
                if (res.data.code === 200) {
                    res.data.message && uni.showToast({ 
                        title: res.data.message, 
                        icon: 'success' 
                    });
                    resolve(res.data);
                } else {
                    const errorHandlers = {
                        401: () => {
                            userStore.clearUser()
                            uni.showModal({
                                title: '登录过期',
                                content: res.data.message,
                                showCancel: false,
                                success: () => {
                                    if (!options.url.includes('/login')) {
                                        uni.reLaunch({ url: '/pages/login/login' })
                                    }
                                }
                            })
                        },
                        403: () => {
                            uni.showModal({
                                title: '权限不足',
                                content: res.data.message,
                                showCancel: false,
                                success: () => uni.navigateBack()
                            });
                        }
                    };

                    errorHandlers[res.data.code]?.() || uni.showToast({
                        title: res.data.message || '请求发生异常',
                        icon: 'none'
                    });
                    reject(res.data);
                }
            },
            fail: (error) => {
                uni.showToast({
                    title: '请求异常',
                    icon: 'none',
                    duration: 1500
                });
                reject(error);
            },
            complete: () => {
                uni.hideLoading();
            }
        })
    })
}
