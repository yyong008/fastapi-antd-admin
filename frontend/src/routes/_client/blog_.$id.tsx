import { BlogContent } from "@/components/Client/BlogDetail/blog-content";
import { BlogHeader } from "@/components/Client/BlogDetail/blog-header";
import { createFileRoute } from "@tanstack/react-router";
import { getBlogById } from "@/apis/client/blog";

export const Route = createFileRoute("/_client/blog_/$id")({
  component: BlogDetailRoute,
  async loader({ params }) {
    const result: any = await getBlogById(Number(params.id));
    if (result && result.code === 0) {
      return result.data;
    }
  },
});

export function BlogDetailRoute() {
  const _data = Route.useLoaderData();
  const blog = _data;
  return (
    <section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
      <div className="font-sans text-base/loose">
        <BlogHeader blog={blog} />
        <BlogContent content={blog.content} />
      </div>
    </section>
  );
}
