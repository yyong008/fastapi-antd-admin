/* prettier-ignore-start */

/* eslint-disable */

// @ts-nocheck

// noinspection JSUnusedGlobalSymbols

// This file is auto-generated by TanStack Router

// Import Routes

import { Route as rootRoute } from './routes/__root'
import { Route as AdminImport } from './routes/admin'
import { Route as ClientImport } from './routes/_client'
import { Route as ClientIndexImport } from './routes/_client/index'
import { Route as ClientNewsImport } from './routes/_client/news'
import { Route as ClientBlogImport } from './routes/_client/blog'
import { Route as ClientAboutImport } from './routes/_client/about'
import { Route as AdminDashboardIndexImport } from './routes/admin/dashboard/index'
import { Route as AdminSystemUserImport } from './routes/admin/system/user'
import { Route as AdminSystemDeptImport } from './routes/admin/system/dept'
import { Route as authAdminLoginImport } from './routes/(auth)/admin.login'
import { Route as AdminSystemMonitorServeImport } from './routes/admin/system/monitor/serve'
import { Route as AdminSystemMonitorLoginLogImport } from './routes/admin/system/monitor/login-log'

// Create/Update Routes

const AdminRoute = AdminImport.update({
  path: '/admin',
  getParentRoute: () => rootRoute,
} as any)

const ClientRoute = ClientImport.update({
  id: '/_client',
  getParentRoute: () => rootRoute,
} as any)

const ClientIndexRoute = ClientIndexImport.update({
  path: '/',
  getParentRoute: () => ClientRoute,
} as any)

const ClientNewsRoute = ClientNewsImport.update({
  path: '/news',
  getParentRoute: () => ClientRoute,
} as any)

const ClientBlogRoute = ClientBlogImport.update({
  path: '/blog',
  getParentRoute: () => ClientRoute,
} as any)

const ClientAboutRoute = ClientAboutImport.update({
  path: '/about',
  getParentRoute: () => ClientRoute,
} as any)

const AdminDashboardIndexRoute = AdminDashboardIndexImport.update({
  path: '/dashboard/',
  getParentRoute: () => AdminRoute,
} as any)

const AdminSystemUserRoute = AdminSystemUserImport.update({
  path: '/system/user',
  getParentRoute: () => AdminRoute,
} as any)

const AdminSystemDeptRoute = AdminSystemDeptImport.update({
  path: '/system/dept',
  getParentRoute: () => AdminRoute,
} as any)

const authAdminLoginRoute = authAdminLoginImport.update({
  path: '/admin/login',
  getParentRoute: () => rootRoute,
} as any)

const AdminSystemMonitorServeRoute = AdminSystemMonitorServeImport.update({
  path: '/system/monitor/serve',
  getParentRoute: () => AdminRoute,
} as any)

const AdminSystemMonitorLoginLogRoute = AdminSystemMonitorLoginLogImport.update(
  {
    path: '/system/monitor/login-log',
    getParentRoute: () => AdminRoute,
  } as any,
)

// Populate the FileRoutesByPath interface

declare module '@tanstack/react-router' {
  interface FileRoutesByPath {
    '/_client': {
      id: '/_client'
      path: ''
      fullPath: ''
      preLoaderRoute: typeof ClientImport
      parentRoute: typeof rootRoute
    }
    '/admin': {
      id: '/admin'
      path: '/admin'
      fullPath: '/admin'
      preLoaderRoute: typeof AdminImport
      parentRoute: typeof rootRoute
    }
    '/_client/about': {
      id: '/_client/about'
      path: '/about'
      fullPath: '/about'
      preLoaderRoute: typeof ClientAboutImport
      parentRoute: typeof ClientImport
    }
    '/_client/blog': {
      id: '/_client/blog'
      path: '/blog'
      fullPath: '/blog'
      preLoaderRoute: typeof ClientBlogImport
      parentRoute: typeof ClientImport
    }
    '/_client/news': {
      id: '/_client/news'
      path: '/news'
      fullPath: '/news'
      preLoaderRoute: typeof ClientNewsImport
      parentRoute: typeof ClientImport
    }
    '/_client/': {
      id: '/_client/'
      path: '/'
      fullPath: '/'
      preLoaderRoute: typeof ClientIndexImport
      parentRoute: typeof ClientImport
    }
    '/(auth)/admin/login': {
      id: '/admin/login'
      path: '/admin/login'
      fullPath: '/admin/login'
      preLoaderRoute: typeof authAdminLoginImport
      parentRoute: typeof rootRoute
    }
    '/admin/system/dept': {
      id: '/admin/system/dept'
      path: '/system/dept'
      fullPath: '/admin/system/dept'
      preLoaderRoute: typeof AdminSystemDeptImport
      parentRoute: typeof AdminImport
    }
    '/admin/system/user': {
      id: '/admin/system/user'
      path: '/system/user'
      fullPath: '/admin/system/user'
      preLoaderRoute: typeof AdminSystemUserImport
      parentRoute: typeof AdminImport
    }
    '/admin/dashboard/': {
      id: '/admin/dashboard/'
      path: '/dashboard'
      fullPath: '/admin/dashboard'
      preLoaderRoute: typeof AdminDashboardIndexImport
      parentRoute: typeof AdminImport
    }
    '/admin/system/monitor/login-log': {
      id: '/admin/system/monitor/login-log'
      path: '/system/monitor/login-log'
      fullPath: '/admin/system/monitor/login-log'
      preLoaderRoute: typeof AdminSystemMonitorLoginLogImport
      parentRoute: typeof AdminImport
    }
    '/admin/system/monitor/serve': {
      id: '/admin/system/monitor/serve'
      path: '/system/monitor/serve'
      fullPath: '/admin/system/monitor/serve'
      preLoaderRoute: typeof AdminSystemMonitorServeImport
      parentRoute: typeof AdminImport
    }
  }
}

// Create and export the route tree

interface ClientRouteChildren {
  ClientAboutRoute: typeof ClientAboutRoute
  ClientBlogRoute: typeof ClientBlogRoute
  ClientNewsRoute: typeof ClientNewsRoute
  ClientIndexRoute: typeof ClientIndexRoute
}

const ClientRouteChildren: ClientRouteChildren = {
  ClientAboutRoute: ClientAboutRoute,
  ClientBlogRoute: ClientBlogRoute,
  ClientNewsRoute: ClientNewsRoute,
  ClientIndexRoute: ClientIndexRoute,
}

const ClientRouteWithChildren =
  ClientRoute._addFileChildren(ClientRouteChildren)

interface AdminRouteChildren {
  AdminSystemDeptRoute: typeof AdminSystemDeptRoute
  AdminSystemUserRoute: typeof AdminSystemUserRoute
  AdminDashboardIndexRoute: typeof AdminDashboardIndexRoute
  AdminSystemMonitorLoginLogRoute: typeof AdminSystemMonitorLoginLogRoute
  AdminSystemMonitorServeRoute: typeof AdminSystemMonitorServeRoute
}

const AdminRouteChildren: AdminRouteChildren = {
  AdminSystemDeptRoute: AdminSystemDeptRoute,
  AdminSystemUserRoute: AdminSystemUserRoute,
  AdminDashboardIndexRoute: AdminDashboardIndexRoute,
  AdminSystemMonitorLoginLogRoute: AdminSystemMonitorLoginLogRoute,
  AdminSystemMonitorServeRoute: AdminSystemMonitorServeRoute,
}

const AdminRouteWithChildren = AdminRoute._addFileChildren(AdminRouteChildren)

export interface FileRoutesByFullPath {
  '': typeof ClientRouteWithChildren
  '/admin': typeof AdminRouteWithChildren
  '/about': typeof ClientAboutRoute
  '/blog': typeof ClientBlogRoute
  '/news': typeof ClientNewsRoute
  '/': typeof ClientIndexRoute
  '/admin/login': typeof authAdminLoginRoute
  '/admin/system/dept': typeof AdminSystemDeptRoute
  '/admin/system/user': typeof AdminSystemUserRoute
  '/admin/dashboard': typeof AdminDashboardIndexRoute
  '/admin/system/monitor/login-log': typeof AdminSystemMonitorLoginLogRoute
  '/admin/system/monitor/serve': typeof AdminSystemMonitorServeRoute
}

export interface FileRoutesByTo {
  '/admin': typeof AdminRouteWithChildren
  '/about': typeof ClientAboutRoute
  '/blog': typeof ClientBlogRoute
  '/news': typeof ClientNewsRoute
  '/': typeof ClientIndexRoute
  '/admin/login': typeof authAdminLoginRoute
  '/admin/system/dept': typeof AdminSystemDeptRoute
  '/admin/system/user': typeof AdminSystemUserRoute
  '/admin/dashboard': typeof AdminDashboardIndexRoute
  '/admin/system/monitor/login-log': typeof AdminSystemMonitorLoginLogRoute
  '/admin/system/monitor/serve': typeof AdminSystemMonitorServeRoute
}

export interface FileRoutesById {
  __root__: typeof rootRoute
  '/_client': typeof ClientRouteWithChildren
  '/admin': typeof AdminRouteWithChildren
  '/_client/about': typeof ClientAboutRoute
  '/_client/blog': typeof ClientBlogRoute
  '/_client/news': typeof ClientNewsRoute
  '/_client/': typeof ClientIndexRoute
  '/admin/login': typeof authAdminLoginRoute
  '/admin/system/dept': typeof AdminSystemDeptRoute
  '/admin/system/user': typeof AdminSystemUserRoute
  '/admin/dashboard/': typeof AdminDashboardIndexRoute
  '/admin/system/monitor/login-log': typeof AdminSystemMonitorLoginLogRoute
  '/admin/system/monitor/serve': typeof AdminSystemMonitorServeRoute
}

export interface FileRouteTypes {
  fileRoutesByFullPath: FileRoutesByFullPath
  fullPaths:
    | ''
    | '/admin'
    | '/about'
    | '/blog'
    | '/news'
    | '/'
    | '/admin/login'
    | '/admin/system/dept'
    | '/admin/system/user'
    | '/admin/dashboard'
    | '/admin/system/monitor/login-log'
    | '/admin/system/monitor/serve'
  fileRoutesByTo: FileRoutesByTo
  to:
    | '/admin'
    | '/about'
    | '/blog'
    | '/news'
    | '/'
    | '/admin/login'
    | '/admin/system/dept'
    | '/admin/system/user'
    | '/admin/dashboard'
    | '/admin/system/monitor/login-log'
    | '/admin/system/monitor/serve'
  id:
    | '__root__'
    | '/_client'
    | '/admin'
    | '/_client/about'
    | '/_client/blog'
    | '/_client/news'
    | '/_client/'
    | '/admin/login'
    | '/admin/system/dept'
    | '/admin/system/user'
    | '/admin/dashboard/'
    | '/admin/system/monitor/login-log'
    | '/admin/system/monitor/serve'
  fileRoutesById: FileRoutesById
}

export interface RootRouteChildren {
  ClientRoute: typeof ClientRouteWithChildren
  AdminRoute: typeof AdminRouteWithChildren
  authAdminLoginRoute: typeof authAdminLoginRoute
}

const rootRouteChildren: RootRouteChildren = {
  ClientRoute: ClientRouteWithChildren,
  AdminRoute: AdminRouteWithChildren,
  authAdminLoginRoute: authAdminLoginRoute,
}

export const routeTree = rootRoute
  ._addFileChildren(rootRouteChildren)
  ._addFileTypes<FileRouteTypes>()

/* prettier-ignore-end */

/* ROUTE_MANIFEST_START
{
  "routes": {
    "__root__": {
      "filePath": "__root.tsx",
      "children": [
        "/_client",
        "/admin",
        "/admin/login"
      ]
    },
    "/_client": {
      "filePath": "_client.tsx",
      "children": [
        "/_client/about",
        "/_client/blog",
        "/_client/news",
        "/_client/"
      ]
    },
    "/admin": {
      "filePath": "admin.tsx",
      "children": [
        "/admin/system/dept",
        "/admin/system/user",
        "/admin/dashboard/",
        "/admin/system/monitor/login-log",
        "/admin/system/monitor/serve"
      ]
    },
    "/_client/about": {
      "filePath": "_client/about.tsx",
      "parent": "/_client"
    },
    "/_client/blog": {
      "filePath": "_client/blog.tsx",
      "parent": "/_client"
    },
    "/_client/news": {
      "filePath": "_client/news.tsx",
      "parent": "/_client"
    },
    "/_client/": {
      "filePath": "_client/index.tsx",
      "parent": "/_client"
    },
    "/admin/login": {
      "filePath": "(auth)/admin.login.tsx"
    },
    "/admin/system/dept": {
      "filePath": "admin/system/dept.tsx",
      "parent": "/admin"
    },
    "/admin/system/user": {
      "filePath": "admin/system/user.tsx",
      "parent": "/admin"
    },
    "/admin/dashboard/": {
      "filePath": "admin/dashboard/index.tsx",
      "parent": "/admin"
    },
    "/admin/system/monitor/login-log": {
      "filePath": "admin/system/monitor/login-log.tsx",
      "parent": "/admin"
    },
    "/admin/system/monitor/serve": {
      "filePath": "admin/system/monitor/serve.tsx",
      "parent": "/admin"
    }
  }
}
ROUTE_MANIFEST_END */
