<template>
	<view class="wrapper">
		<app-layout>
			<template #main>
				<view class="container">
					<!-- 统计卡片 -->
					<view class="count-card">
						<view class="section-title">我的数据</view>
						<uni-grid :column="4" :highlight="true" :square="false" @change="">
							<uni-grid-item v-for="(item, index) in stats" :key="index">
								<view class="stat-item" @click="handleStatClick(index)">
									<text class="stat-number">{{ item.value }}</text>
									<text class="stat-label">{{ item.label }}</text>
								</view>
							</uni-grid-item>
						</uni-grid>
					</view>

					<!-- 功能列表 -->
					<view class="function-list">
						<uni-list>
							<uni-list-item v-for="(item, index) in menuItems" :key="index" :show-arrow="item.showArrow"
								:title="item.title" :link="item.link" :to="item.to"
								@click.native="handleMenuClick(item)">
								<template v-if="item.badge" #footer>
									<uni-badge :text="item.badge" type="error" size="small" />
								</template>
							</uni-list-item>
						</uni-list>
					</view>
				</view>
			</template>
		</app-layout>
	</view>
</template>

<script setup>
import { ref } from 'vue';

// 统计数据
const stats = ref([
	{ value: 8, label: '收藏影视' },
	{ value: 14, label: '历史记录' },
	{ value: 18, label: '关注信息' },
	{ value: 84, label: '我的足迹' }
]);

// 菜单项
const menuItems = ref([
	{ title: '我的消息', showArrow: true, badge: '3' },
	{ title: '意见反馈', showArrow: true },
	{ title: '分享链接', showArrow: true, action: 'share' },
	{ title: '关于我们', showArrow: true, to: '/pages/about/about?item=2' }
]);

// 处理统计项点击
const handleStatClick = (index) => {
	uni.showToast({
		title: `点击了${stats.value[index].label}`,
		icon: 'none'
	});
	// 这里可以添加跳转逻辑
};

// 处理菜单点击
const handleMenuClick = (item) => {
	if (item.action === 'share') {
		uni.share({
			provider: 'weixin',
			type: 0,
			title: '分享标题',
			summary: '分享内容',
			success: (res) => {
				console.log('分享成功', res);
			}
		});
	}
};
</script>

<style scoped lang="scss">
.container {
	padding: 20rpx;

	.section-title {
		font-size: 28rpx;
		font-weight: 500;
		color: #666;
		margin-bottom: 20rpx;
		padding: 0 20rpx;
	}

	/* 统计卡片样式 */
	.count-card {
		margin-bottom: 30rpx;

		:deep(.uni-grid) {
			background: #fff;
			border-radius: 16rpx;
			box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.05);
			overflow: hidden;
		}

		.stat-item {
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
			padding: 30rpx 0;
			transition: all 0.2s ease;

			&:active {
				background-color: #f7f7f7;
			}

			.stat-number {
				font-size: 36rpx;
				font-weight: 600;
				color: #333;
				margin-bottom: 8rpx;
			}

			.stat-label {
				font-size: 24rpx;
				color: #999;
			}
		}
	}

	/* 功能列表样式 */
	.function-list {
		background: #fff;
		border-radius: 16rpx;
		box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.05);
		overflow: hidden;

		:deep(.uni-list-item) {
			padding: 28rpx 30rpx;
			border-bottom: 1rpx solid #f5f5f5;

			&:last-child {
				border-bottom: none;
			}

			&:active {
				background-color: #f7f7f7;
			}

			.uni-list-item__container {
				height: auto;
				min-height: 80rpx;
			}
		}
	}
}
</style>