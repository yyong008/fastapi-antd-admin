import { BlogItem } from "@/components/Client/Blog/blog-item";
import { createFileRoute } from "@tanstack/react-router";
import { getBlogList } from "@/apis/client/blog";

export const Route = createFileRoute("/_client/blog")({
  component: BlogRoute,
  loaderDeps: ({ search }: any) => ({
    page: search.page || 1,
    pageSize: search.pageSize || 10,
  }),
  async loader({ deps }) {
    const result: any = await getBlogList({
      page: deps.page,
      pageSize: deps.pageSize,
    });
    if (result && result.code === 0) {
      return result.data;
    }
  },
});

export function BlogRoute() {
  const _data = Route.useLoaderData();
  const blogs = _data.list;

  return (
    <section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
      <div className="mb-6">
        <h1 className="text-2xl font-semibold text-slate-900">Blog</h1>
        <p className="mt-2 text-sm text-slate-500">Product insights and technical articles.</p>
      </div>
      <div className="space-y-2">
        {blogs?.map((n: any) => {
          return <BlogItem data={n} key={n.id} />;
        })}
      </div>
    </section>
  );
}
