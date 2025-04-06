<template>
	<app-layout>
		<template #main>
			<view class="work-container">
				<!-- 搜索和新增按钮区域 -->
				<view class="header-actions">
					<up-search 
						:placeholder="'搜索用户'" 
						v-model="pageQuery.name" 
						:show-action="false"
						@search="handleUserList" 
						@clear="handleClearSearch" 
						class="search-box"
					/>
					<up-button 
						type="primary" 
						text="新增" 
						size="small"
						icon="plus" 
						@click="navigateTo('create')"
						class="add-button"
						shape="circle"
					/>
				</view>

				<!-- 列表容器 -->
				<up-list :border="false" height="auto">
					<up-list-item v-for="item in tableData" :key="item.id">
						<up-cell :border="false" >
							<template #icon>
								<up-avatar shape="circle" size="35"
									:src="item.avatar || '/static/default-avatar.png'"
									custom-style="margin-right: 10rpx"></up-avatar>
							</template>
							<template #title>
								<view class="cell-content">
									<up-text class="name" type="primary" :text="item.name" @click.="navigateTo(`detail?id=${item.id}`)"></up-text>
								</view>
							</template>
							<template #label>
								<view class="tag-group">
										<up-tag :type="item.disabled ? 'warning' : 'success'" size="mini"
											:text="item.disabled ? '禁用' : '启用'" custom-style="margin-left: 8rpx" plain plainFill />
										<up-tag v-if="item.is_superuser" type="info" size="mini" text="管理员" plain plainFill
											custom-style="margin-left: 8rpx" />
									</view>
							</template>
							<template #right-icon>
								<view class="action-group">
									
									<view class="button-group">
										<up-button
											:disabled="item.is_superuser" 
											type="primary" 
											size="mini" 
											text="编辑"
											@click="navigateTo(`update?id=${item.id}`)"
										/>
										<up-button 
											:disabled="item.is_superuser"
											type="error" 
											size="mini" 
											text="删除"
											@click="handleDeleteUser(item)"
										/>
									</view>
								</view>
							</template>
						</up-cell>
					</up-list-item>
				</up-list>
				<!-- 加载更多 -->
				<up-loadmore 
					:status="loadStatus" 
					:load-text="{ loadmore: '上拉或点击加载更多' }" 
					@loadmore="loadMore" 
				/>
				<!-- 空数据提示 -->
				<up-empty v-if="pagination.total === 0" mode="data" text="暂无用户数据"></up-empty>
			</view>
		</template>
	</app-layout>
</template>

<script setup>
import { ref, reactive } from "vue";
import { onLoad, onShow } from '@dcloudio/uni-app';
import { list_user, delete_user } from "@/api/apis";

// 响应式数据
const loadStatus = ref('loadmore');
const tableData = ref([]);
const pageQuery = ref({
	name: '',
	offset: 0,
	limit: 8
});
// 分页配置
const pagination = reactive({
	total: 0, // 总数据条数
	hasNext: null, // 是否有下一页
});

// 初始化加载
onLoad(() => {
	handleUserList();
});

onShow(() => {
	// 页面重新显示时，重置查询条件
	pageQuery.value.offset = 0;
	handleUserList();
});

// 获取用户列表
const handleUserList = async () => {
	loadStatus.value = 'loading';
	
	const result = await list_user(pageQuery.value);
	// 确保 API 返回的数据结构正确
	if (result && result.data.items) {
		if (pageQuery.value.offset === 0) {
			tableData.value = result.data.items;
		} else {
			tableData.value = [...tableData.value, ...result.data.items];
		}
		// 更新分页状态
		pagination.hasNext = result.data.has_next;
		pagination.total = result.data.total;
		loadStatus.value = pagination.hasNext ? 'loadmore' : 'nomore';
	} else {
		throw new Error('API 数据结构异常');
	}
};

// 删除用户
const handleDeleteUser = async (item) => {
	uni.showModal({
		title: '确认删除',
		content: `确定要删除用户 "${item.name}" 吗？`,
		confirmColor: '#e45656',
		success: async (res) => {
			if (res.confirm) {
				await delete_user(item.id);
				// 重新加载用户列表
				pageQuery.value.offset = 0;
				handleUserList();
			}
		}
	});
};

// 加载更多
const loadMore = () => {
	if (pagination.hasNext && loadStatus.value === 'loadmore') {
		pageQuery.value.offset += pageQuery.value.limit;
		handleUserList();
	}
};

// 清除搜索框时重置查询条件并重新加载数据
const handleClearSearch = () => {
	pageQuery.value.name = '';
	pageQuery.value.offset = 0;
	handleUserList();
};

// 新增页面：create 、 编辑页面： update 、详情页面：detail
const navigateTo = (page) => {
    uni.navigateTo({ url: `/pages/work/${page}` })
}
</script>

<style lang="scss" scoped>
.work-container {
	padding: 30rpx;
	
	.header-actions {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 20rpx;
		gap: 30rpx;
		
		.search-box {
			flex: 1;
			min-width: 0; // 防止搜索框溢出
		}
		
		.add-button {
			flex: none;
			width: 140rpx;
		}
	}
	
	.action-group {
		display: flex;
		align-items: center;
		gap: 20rpx;
	}
	
	.button-group {
		display: flex;
		gap: 10rpx;
	}
	
	.name {
		color: #2979ff;
		
		&:active {
			opacity: 0.7;
		}
	}
}
</style>