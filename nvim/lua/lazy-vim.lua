local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
	vim.fn.system({
		"git",
		"clone",
		"--filter=blob:none",
		"https://github.com/folke/lazy.nvim.git",
		"--branch=stable", -- latest stable release
		lazypath,
	})
end
vim.opt.rtp:prepend(lazypath)

require('lazy').setup({

	-- Comment plugin (gcc)
	{ 
		'numToStr/Comment.nvim', opts = {}
	},

	-- Telescope
	{
		'nvim-telescope/telescope.nvim', tag = '0.1.4',
		dependencies = { 'nvim-lua/plenary.nvim' }
	},

	-- Statusline
	{
		'nvim-lualine/lualine.nvim',
		opts = {
			options = {
				icons_enabled = true,
				theme = 'moonfly',
			},
		},
	},

	-- Theme
	{
		'bluz71/vim-moonfly-colors',
		priority = 1000,
		config = function()
			vim.cmd.colorscheme 'moonfly'
		end,
	},

	-- Nvim-treesitter
	{
		"nvim-treesitter/nvim-treesitter", build = ":TSUpdate"
	},

	-- LSP Mason CMP
	{'VonHeikemen/lsp-zero.nvim', branch = 'v3.x'},
	{'williamboman/mason.nvim'},
	{'williamboman/mason-lspconfig.nvim'},
	{'neovim/nvim-lspconfig'},
	{'hrsh7th/cmp-nvim-lsp'},
	{'hrsh7th/nvim-cmp'},
	{'L3MON4D3/LuaSnip'},
})
