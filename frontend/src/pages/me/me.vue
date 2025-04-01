<template>
	<view class="wrapper">
		<app-layout>

			<template #main>

				<!-- 统计 -->
				<view class="count">
					<view class="count-title">我的数据</view>
					<uni-grid :column="4" :highlight="true" :square="false" @change="">
						<uni-grid-item>
							<view class="count-item">
								<text class="num">8</text>
								<text class="label">收藏影视</text>
							</view>
						</uni-grid-item>
						<uni-grid-item>
							<view class="count-item">
								<text class="num">14</text>
								<text class="label">历史记录</text>
							</view>
						</uni-grid-item>
						<uni-grid-item>
							<view class="count-item">
								<text class="num">18</text>
								<text class="label">关注信息</text>
							</view>
						</uni-grid-item>
						<uni-grid-item>
							<view class="count-item">
								<text class="num">84</text>
								<text class="label">我的足迹</text>
							</view>
						</uni-grid-item>
					</uni-grid>
				</view>

				<!-- 其它 -->
				<view class="extra">
					<uni-list>
						<uni-list-item showArrow title="我的消息"></uni-list-item>
						<uni-list-item showArrow title="意见反馈"></uni-list-item>
						<uni-list-item showArrow title="分享链接" @click.native="onShareClick($event, 1)" link></uni-list-item>
						<uni-list-item showArrow title="关于我们" link to="/pages/about/about?item=2"></uni-list-item>
					</uni-list>
				</view>

			</template>
		</app-layout>
	</view>
</template>

<script setup>
import { ref } from "vue";
import { onReady } from "@dcloudio/uni-app";
import { detail_user } from "../../api/apis";
const formData = ref({
	id: null,
	name: "",
	username: "",
	password: "",
	disabled: null,
	is_superuser: null,
	avatar: "https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png",
	description: "",
	parent_id: null,
	created_at: "",
	updated_at: "",
});



// 加载数据
onReady(() => {
	handleDetail();
});

// 获取用户详情
async function handleDetail() {
	const res = await detail_user(uni.getStorageSync('user_id'));
	console.log('用户详情', res);
	formData.value = res.data;
}


</script>


<style scoped lang="scss">
.wrapper {
	padding: 0;
}

.count {
	margin: 20rpx 0;
	background: transparent;
	padding: 0;

	.count-title {
		font-size: 28rpx;
		font-weight: 500;
		color: #666;
		margin-bottom: 15rpx;
		padding: 0 20rpx;
	}

	:deep(.uni-grid) {
		border: none;
		background: #fff;
		border-radius: 12rpx;
		margin: 0 20rpx;
		padding: 10rpx 0;
	}

	:deep(.uni-grid-item) {
		.count-item {
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
			padding: 15rpx 0;

			.num {
				font-size: 32rpx;
				font-weight: 500;
				color: #333;
				margin-bottom: 8rpx;
			}

			.label {
				font-size: 22rpx;
				color: #999;
			}
		}
	}
}

.extra {
	margin-top: 20rpx;
	background: #fff;
	border-radius: 12rpx;
	margin: 0 20rpx;

	:deep(.uni-list-item) {
		padding: 20rpx 25rpx;
		border-bottom: 1rpx solid #f5f5f5;

		&:last-child {
			border-bottom: none;
		}

		&:active {
			background-color: #f9f9f9;
		}
	}
}




</style>
