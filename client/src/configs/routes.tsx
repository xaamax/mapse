import { createBrowserRouter, Navigate } from "react-router-dom";
import { DashboardLayout } from "@/layouts/dashboard/dashboard-layout";
import RootLayout from "@/layouts/root/root-layout";
import { Login, Dashboard, ProjetosSociais, ProjetoSocialDetalhes, Error404 } from "@/pages/index";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <RootLayout />,
    children: [
      {
        path: "",
        element: <DashboardLayout />,
        children: [
          {
            index: true,
            element: <Navigate to="/dashboard" replace />,
          },
          {
            path: "dashboard",
            element: <Dashboard />,
          },
          {
            path: "projetos-sociais",
            children: [
              {
                path: "",
                element: <ProjetosSociais />,
              },
              {
                path: "incluir",
                element: <ProjetoSocialDetalhes />,
              },
            ],
          },
        ],
      },
    ],
  },
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/*",
    element: <Error404 />,
  },
]);
