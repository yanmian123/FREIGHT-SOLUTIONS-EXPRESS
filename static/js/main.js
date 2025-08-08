// 新增：表单显示/隐藏功能
document.addEventListener('DOMContentLoaded', function () {
    const showFormBtn = document.getElementById('showQuoteForm');
    const formContainer = document.getElementById('quoteFormContainer');

    if (showFormBtn && formContainer) {
        showFormBtn.addEventListener('click', function () {
            // 显示表单
            formContainer.classList.add('active');

            // 滚动到表单位置
            formContainer.scrollIntoView({
                behavior: 'smooth'
            });

            // 隐藏按钮
            showFormBtn.style.display = 'none';
        });
    }
});

// 平滑滚动
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        if (targetId === '#hero') {
            document.querySelector('.hero').scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// 表单提交处理（改为 AJAX 方式）
document.querySelector('.quote-form').addEventListener('submit', function (e) {
    e.preventDefault(); // 继续阻止默认跳转

    // 获取表单数据
    const formData = new FormData(this);

    // 发送 AJAX 请求到 Django 视图
    fetch(window.location.href, {  // 提交到当前页面的 URL（即 Django 的 index 视图）
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value  // 传递 CSRF Token
        }
    })
        .then(response => response.text())
        .then(data => {
            alert(data);  // 显示 Django 返回的响应（如 "Submission successful!"）
            this.reset(); // 重置表单
        })
        .catch(error => {
            console.error('提交失败:', error);
            alert('Submission failed. Please try again.');
        });
});

// 图片懒加载初始化（依赖lazysizes库）
if ('lazysizes' in window) {
    lazysizes.init();
}

// 页面加载完成后添加动画效果
window.addEventListener('load', function () {
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';

        // 延迟显示以创建顺序动画
        setTimeout(() => {
            section.style.opacity = '1';
            section.style.transform = 'translateY(0)';
        }, 100);
    });
});


// 关于我们展开/收起功能（流畅动画版）
document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.querySelector('.about-toggle');
    const detailsContainer = document.querySelector('.about-details');
    const header = document.querySelector('.header');
    const headerHeight = header ? header.offsetHeight : 0;

    if (toggleBtn && detailsContainer) {
        // 初始化状态
        detailsContainer.style.maxHeight = '0';
        detailsContainer.style.overflow = 'hidden';
        detailsContainer.style.opacity = '0';
        detailsContainer.style.paddingTop = '0';
        detailsContainer.style.paddingBottom = '0';
        detailsContainer.style.transition = 'max-height 0.5s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.5s ease, padding 0.5s ease';

        // 存储元素原始样式，避免重复获取
        const originalStyles = {
            paddingTop: detailsContainer.style.paddingTop,
            paddingBottom: detailsContainer.style.paddingBottom,
            overflow: detailsContainer.style.overflow
        };

        toggleBtn.addEventListener('click', function () {
            const isExpanded = detailsContainer.style.maxHeight !== '0px' && detailsContainer.style.maxHeight;

            if (isExpanded) {
                // 收起逻辑 - 保持不变
                detailsContainer.style.maxHeight = '0';
                detailsContainer.style.opacity = '0';
                detailsContainer.style.paddingTop = '0';
                detailsContainer.style.paddingBottom = '0';
                toggleBtn.textContent = 'Click to expend';
                toggleBtn.classList.remove('active');
            } else {
                // 关键优化：使用不可见区域计算高度，避免视觉闪烁
                // 创建一个克隆元素用于计算高度
                const clone = detailsContainer.cloneNode(true);
                clone.style.position = 'absolute';
                clone.style.visibility = 'hidden'; // 不可见但保留空间
                clone.style.maxHeight = 'none';
                clone.style.opacity = '0';
                clone.style.overflow = 'visible';
                clone.style.paddingTop = '30px';
                clone.style.paddingBottom = '30px';

                // 添加到文档中进行计算
                document.body.appendChild(clone);
                const realHeight = clone.scrollHeight;

                // 移除克隆元素
                document.body.removeChild(clone);

                // 执行展开动画
                detailsContainer.style.maxHeight = "none";
                detailsContainer.style.opacity = '1';
                detailsContainer.style.paddingTop = '30px';
                detailsContainer.style.paddingBottom = '30px';

                // 计算滚动位置
                const rect = detailsContainer.getBoundingClientRect();
                const targetScroll = window.pageYOffset + rect.top - 100 - headerHeight;

                // 执行滚动
                setTimeout(() => {
                    window.scrollTo({
                        top: targetScroll,
                        behavior: 'smooth'
                    });
                }, 100);

                toggleBtn.textContent = 'Click to hide';
                toggleBtn.classList.add('active');
            }
        });
    }
});


// 在现有脚本下方添加
const inquiryToggleBtn = document.getElementById('toggleInquiryForm');
const inquiryFormContainer = document.getElementById('inquiryFormContainer');

// 等待DOM加载完成
document.addEventListener('DOMContentLoaded', function () {
    // 导航区按钮（保留原逻辑）
    document.getElementById('toggleQuoteForm').addEventListener('click', function () {
        document.getElementById('quoteModal').style.display = 'block';
    });
    document.getElementById('toggleInquiryForm').addEventListener('click', function () {
        document.getElementById('inquiryModal').style.display = 'block';
    });

    // 新增：英雄区按钮的事件绑定
    document.getElementById('heroToggleQuoteForm').addEventListener('click', function () {
        document.getElementById('quoteModal').style.display = 'block';
    });
    document.getElementById('heroToggleInquiryForm').addEventListener('click', function () {
        document.getElementById('inquiryModal').style.display = 'block';
    });

    // 关闭弹窗的逻辑（假设已有，确保能正常关闭）
    document.querySelectorAll('.close-modal').forEach(button => {
        button.addEventListener('click', function () {
            document.getElementById('quoteModal').style.display = 'none';
            document.getElementById('inquiryModal').style.display = 'none';
        });
    });
});

// 补充英雄区按钮的事件绑定
const heroToggleQuoteBtn = document.getElementById('heroToggleQuoteForm');
const heroToggleInquiryBtn = document.getElementById('heroToggleInquiryForm');

heroToggleQuoteBtn.addEventListener('click', function () {
    quoteModal.style.display = 'flex';
    // document.body.style.overflow = 'hidden'; // 禁止背景滚动
});

heroToggleInquiryBtn.addEventListener('click', function () {
    inquiryModal.style.display = 'flex';
    // document.body.style.overflow = 'hidden'; // 禁止背景滚动
});
