import { useUserStore } from "../stores/index";

export function request(options) {
    const userStore = useUserStore();
    uni.showToast({
        title: "加载中...",
        icon: "loading",
        mask: true,
    });

    return new Promise((resolve, reject) => {
        // 处理文件上传
        if (options.filePath) {
            uni.uploadFile({
                url: import.meta.env.VITE_API_BASE_URL + options.url,
                method: options.method || "POST",
                filePath: options.filePath,
                name: "file",
                header: {
                    Authorization: userStore.token ? `Bearer ${userStore.token}` : "",
                    // 移除 Content-Type，让 uni.uploadFile 自动处理 multipart/form-data
                },
                success: (res) => {
                    const result = JSON.parse(res.data); // 解析返回的 JSON 数据
                    if (result.code === 200) {
                        uni.showToast({
                            title: result.message || '上传成功',
                            icon: "success",
                            mask: true,
                        });
                        resolve(result);
                    } else {
                        uni.showToast({
                            title: result.message || "上传失败",
                            icon: "none",
                            mask: true,
                        });
                        reject(result);
                    }
                },
                fail: (error) => {
                    console.error('上传失败:', error);
                    uni.showToast({
                        title: "上传失败",
                        icon: "none",
                    });
                    reject(error);
                },
            });
            return;
        }

        // 普通请求处理
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
                    userStore.clear();
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
            },
        });
    });
}
