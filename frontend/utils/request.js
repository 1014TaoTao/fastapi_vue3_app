let loadingCount = 0;
export function request(options){
	if (++loadingCount === 1) {
        uni.showLoading({
            title: '加载中...',
            mask: true,
            icon: 'loading'
        }); 
    }
    loadingCount++; 

	return new Promise((resolve, reject) => {
		uni.request({
			url: import.meta.env.VITE_API_BASE_URL + options.url,
			method: options.method || "GET",
			data: options.data || "",
			header: {
				// 'content-type': 'application/json',
                'Authorization': 'Bearer ' + uni.getStorageSync('token') || '',
                ...options.header || {}
			},
            timeout: import.meta.env.VITE_TIMEOUT,
			success: (res) => {
                if (res.data.code === 200) {
                    console.log('成功', res.data);
                    uni.showToast({ title: '成功', icon: 'success' });
                    resolve(res.data);
                } else if (res.data.code === 401) {
                    uni.removeStorageSync("token");
                    uni.showModal({ 
                        title: '登录过期',
                        content: '登录已过期，请重新登录',
                        showCancel: false,
                        success: () => {
                            uni.reLaunch({ url: '/pages/login/login' });
                        }
                    });
                    reject(res.data);
                } else if (res.data.code === 403) {
                    uni.showModal({ 
                        title: '权限不足',
                        content: '您没有权限访问该资源',
                        showCancel: false,
                        success: () => {
                            uni.navigateBack();
                        }
                    });
                    reject(res.data);
                } else {
                    uni.showToast({ 
                        title: res.data.message || '请求发生异常',
                        icon: 'none'
                    });
                    reject(res.data);
                }
			},
			fail: (error) => {
				reject(error)
				setTimeout(() => {
					uni.showToast({
						title: '请求异常',
						icon: 'none',
						duration: 1500
					})
				}, 500)
			},
			complete() {
                if (--loadingCount === 0) {
                    uni.hideLoading();
                }
            }
		})
	})
}
